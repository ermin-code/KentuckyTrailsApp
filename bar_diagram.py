import pandas as pd   
import plotly          
import plotly.express as px
import plotly.io as pio
from collections import Counter
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np


#------------------------------------------------------------------------
df = pd.read_csv("kentuckytrails.csv")

 # converting column data to list
 #------------------------------------------------------------------------
tn = df['trail_name'].tolist()
ct = df['county'].tolist()
tl = df['trail_length'].tolist()
for i in range(0, len(tl)):
    tl[i] = float(tl[i])
ma = df['maintenance'].tolist()

# counting number of well, fair and poorly maintained trails in kentucky
#------------------------------------------------------------------------
ma_good = int(ma.count("Good"))
ma_fair = int(ma.count("Fair"))
ma_poor = int(ma.count("Poor"))

# finding percentages of well, fair and poorly maintained trails in kentucky
#------------------------------------------------------------------------
ma_total = int((ma_good + ma_poor + ma_fair))
per_ma_good = int(ma_good/ma_total * 100)
per_ma_fair = int(ma_fair/ma_total * 100)
per_ma_poor = int(ma_poor/ma_total *100)

# organizing data into three columns named condition, percentage and color
#------------------------------------------------------------------------
data_cond = ["Good","Fair","Poor"]
data_per = [per_ma_good,per_ma_fair,per_ma_poor]
data_color = ["green","orange","red"]
pie_data =list(zip(data_cond,data_per,data_color))
data_f = pd.DataFrame(pie_data, columns=['Condition','Percentage','Color'])

# combining 'county' and 'trail length' lists together into one
#------------------------------------------------------------------------
county_trail_length_data =list(zip(ct,tl))
data_county_trail_length = pd.DataFrame(county_trail_length_data, columns=['County','Trail Length'])

# grouping counties by name and summing trail lengths of each county 
#------------------------------------------------------------------------
data_county_trail_length['Total Trail Length'] = data_county_trail_length.groupby(['County'])['Trail Length'].transform('sum')
new_data_county_trail_length = data_county_trail_length.drop_duplicates(subset=['County'])
county_trail_length_chart = new_data_county_trail_length.drop(['Trail Length'], axis=1)
df = pd.DataFrame(county_trail_length_chart)

# plotting bar diagram showing names of counties vs. total trail length for each county
#------------------------------------------------------------------------
df.plot(kind = 'bar',
        x = 'County',
        y = 'Total Trail Length',
        color = 'green')
  
# set the title
plt.title('Total Length of Trails by Kentucky County')
  
# show the plot
plt.show()