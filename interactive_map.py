import pandas as pd
import numpy as np
import dash                    
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as py     
import plotly.graph_objs as go
import webbrowser
import secret

# token for mapbox map access
#---------------------------------------------------------------
#IMPORTANT:
# please note that I protected my mapbox personal token via .gitignore. however, mapbox offers 
# general public default token that you can use to run this code by enabling it below:

mapbox_access_token = 'pk.eyJ1IjoiZXJtaW5reSIsImEiOiJjbDFiM2d1N2sxZTg2M2lud2UxbzVreXFuIn0.KPyZHRZzUN1Ib4i-IoGOrQ'

# you will also need to make changes to the code in line 99. please see below. 


# builds data frame for specific columns within csv file
#---------------------------------------------------------------
df = pd.read_csv("kentuckytrails.csv")
df['county'] = [str(x) for x in df['county']]
df['trail_name'] = [str(x) for x in df['trail_name']]
df['maintenance'] =[str(x) for x in df['maintenance']]

app = dash.Dash(__name__)

blackbold={'color':'black', 'font-weight': 'bold'}

app.layout = html.Div([

# map_legend + county_checklist + trail_condition_checklist + map    
#---------------------------------------------------------------
    html.Div([
        html.Div([
            # Map-legend
            html.Ul([html.Label(children=['Trail Condition Legend: '], style=blackbold),
                html.Li("Good", className='circle', style={'background': 'green','color':'black',
                    'list-style':'none','text-indent': '17px'}),
                html.Li("Fair", className='circle', style={'background': 'orange','color':'black',
                    'list-style':'none','text-indent': '17px','white-space':'nowrap'}),
                html.Li("Poor", className='circle', style={'background': 'red','color':'black',
                    'list-style':'none','text-indent': '17px'}),                
                html.Li("Nan", className='circle', style={'background': 'black','color':'black',
                    'list-style':'none','text-indent': '17px'}),], style={'border-bottom': 'solid 3px', 'border-color':'black','padding-top': '6px'}),

            # County_checklist
            html.Label(children=['Kentucky Counties: '], style=blackbold),
            dcc.Checklist(id='county_name',
                    options=[{'label':str(b),'value':b} for b in sorted(df['county'].unique())],
                    value=[b for b in sorted(df['county'].unique())],),

            # Trail_Condition_checklist
            html.Label(children=['Trail Condition: '], style=blackbold),
            dcc.Checklist(id='maintenance',
                    options=[{'label':str(b),'value':b} for b in sorted(df['maintenance'].unique())],
                    value=[b for b in sorted(df['maintenance'].unique())],),], className='three columns'),

            # Map
            html.Div([
                dcc.Graph(id='graph', config={'displayModeBar': False, 'scrollZoom': True},
                    style={'background':'black','padding-top':'2px', 'padding-bottom':'2px','padding-left':'2px','padding-right':'2px','height':'100vh'})], 
                    className='nine columns'),], className='row'),], className='ten columns offset-by-one')

# output of graph
#---------------------------------------------------------------
@app.callback(Output('graph', 'figure'),
              [Input('county_name', 'value'),
               Input('maintenance', 'value')])

def update_figure(chosen_county,chosen_recycling):
    df_sub = df[(df['county'].isin(chosen_county)) &
                (df['maintenance'].isin(chosen_recycling))]

    # Create figure
    locations=[go.Scattermapbox(
                    lon = df_sub['longitude'],
                    lat = df_sub['latitude'],
                    mode='markers',
                    marker={'color' : df_sub['color']},
                    unselected={'marker' : {'opacity':1}},
                    selected={'marker' : {'opacity':0.5, 'size':25}},
                    hoverinfo='text',
                    hovertext=df_sub['hov_txt'],)]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision= 'foo', #preserves state of figure/map after callback activated
            clickmode= 'event+select',
            hovermode='closest',
            hoverdistance=2,
            title=dict(text="Map of Kentucky Trails",font=dict(size=50, color='black')),
            mapbox=dict(
                #to run public token, please change to accesstoken=mapbox_access_token
                accesstoken=mapbox_access_token, 
                bearing=0,
                style='light',
                center=dict(
                    lat=37.2828,
                    lon=-85.34603
                ),
                pitch=40,
                zoom=6.1
            ),
        )
    }

# callback for Web_link
#---------------------------------------------------------------
@app.callback(
    Output('web_link', 'children'),
    [Input('graph', 'clickData')])
def display_click_data(clickData):
    if clickData is None:
        return 'Click on any bubble'
    else:
        # print (clickData)
        the_link=clickData['points'][0]['customdata']
        if the_link is None:
            return 'No Website Available'
        else:
            return html.A(the_link, href=the_link, target="_blank")

# #--------------------------------------------------------------
if __name__ == '__main__':
    #automatically opens web browser
    webbrowser.open_new('http://127.0.0.1:8050/')
    app.run_server(debug=False)