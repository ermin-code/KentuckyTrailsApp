from flask import Flask, render_template, url_for, request
import csv
import folium 
import pandas as pd
import sys
import webbrowser
from waitress import serve

# application created and __name__ variable is passed to the flask class
#---------------------------------------------------------------

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():

    return render_template("index.html")


@app.route('/result',methods=['POST', 'GET'])

@app.route('/search',methods=['POST', 'GET'])

# searches csv file by entered trail, stores trail coordinates in a variable to be displayed on the map
#---------------------------------------------------------------
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]

    data=[]
    with open("kentuckytrails.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

        col = [x[0] for x in data]
        # trail name search
        if name in col:
            for x in range(0,len(data)):
                #if name mached, stores trail length and coordinates in leng and start_coords variables
                if name == data[x][0]:
                    leng = data[x][2]
                    county = data[x][1]
                    start_coords = (data[x][3],data[x][4])

            #specifies map properties
            folium_map = folium.Map(location=start_coords, zoom_start=16,prefer_canvas=True)
            folium.CircleMarker(location=start_coords,
                        radius=40,
                        weight=8).add_to(folium_map)
            folium_map.save('templates/map.html')
            return render_template('index.html', name = name,leng = leng, county = county)
        
        # displays "No trail found!" if trail name does not match 
        else:
            nonname = "No trail found!"
            return render_template('index.html',nonname = nonname)

if __name__ == "__main__":
#automatically opens web browser 
    webbrowser.open_new('http://127.0.0.1:5000/')
    serve(app, host="127.0.0.1", port=5000)

    
