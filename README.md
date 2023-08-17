# Kentucky Trails App - Python\Data Analytics Project


This project is about presentation and analysis of data on offroad trails in Kentucky obtained through CSV file provide by KyGovMaps Open Data Portal Government website (https://opengisdata.ky.gov/). There are more than 300 trails in the dataset. Organization of the project is best represented in KentuckyTrails.ipynb Jupyter Notebook file, however, following is the general breakdown of different python programs within the project. These individual programs can be run through Visual Studio Code provided that all the required packages are installed. Names of these packages are listed in this ReadMe file. 

(Part 1) - trail_search.py file 
HTML interface that uses a textbox to search name of a particular trail in kentuckytrails.csv file and displays trail location on the map. It also indicates how long the trail is and in which county it is located in. If a wrong trail name is entered or if nothing is entered, a message on the page will be displayed that says 'No Trail Found!'

(Part 2) - interactive_map.py file
HTML interface that displays map of Kentucky showing all trail locations throughout the map. Each dot representing trails is color coded indicating trail condition (green - well maintained, orange - fairly maintained and red - poortly maintained). A black dot on the map indicates a trail that does not have information on its main·te·nance. On the left are selected all the counties in Kentucky that have trail information available. You can select or unselect different counties and maintenance conditions to narrow down the information presented on the map. 

Please note that my personal MapBox token was hiden in .gitignore. However, you can use general public token provided by Mapbox:

mapbox_access_token = 'pk.eyJ1IjoiZXJtaW5reSIsImEiOiJjbDFiM2d1N2sxZTg2M2lud2UxbzVreXFuIn0.KPyZHRZzUN1Ib4i-IoGOrQ'

IMPORTANT: Also, please note that in order to use this token, you need to remove 'import secret' on the top and on line 99 you will need to change the code from secret.accesstoken=mapbox_access_token to accesstoken=mapbox_access_token 

(Part 3) - pie_chart.py file
This is a Python script that uses Pandas and Plotly packages to display a pie chart showing percentages of well, fairly and poorly maintained trails in Kentucky. Data from kentuckytrails.csv file was processed in a way that number of trails associated with these three maintenance conditions were counted and percentages were calculated and displayed in this pie chart. 

(Part 4) - table.py file
This is a Python script that uses Pandas and Plotly packages to display a table showing all the included Kentucky counties in kentuckytrails.csv file and total mileage of trails in each county. Data processing from kentuckytrails.csv file was processed in a way that all the trail lengths for each county were summed up and displayed in this table.  

(Part 5) - bar_diagram.py file
This is a Python script that uses Pandas and MatPlotLib packages to display a bar diagram showing all the included Kentucky counties in kentuckytrails.csv file and total mileage of trails in each county. Data processing from kentuckytrails.csv was processed in a way that all the trail lengths for each county were summed up and displayed in this diagram. 

All four features of this project are executable individually in Visual Studio Code or through Jupyter Notebook by opening KentuckyTrails.ipynb and running each of four individual sections. Reminder: you will need to stop running Kernel every time you want to run a section. Running Kernel of previous section will prevent the next from being run. 

This project is built to meet the following requirements of Python of Code Louisville January 2022 session. 

1. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
2. Visualize data in a graph, chart, or other visual representation of data
3. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
4. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code. To clarify, at least one function should be called in your code, that function should calculate, retrieve, or otherwise set the value of a variable or data structure, return a value to where it was called, and use that value somewhere else in your code. For example, you could create a function that reads how many items there are in a text  file, returns that value, and later uses that value to execute a loop a certain number of times.
5. Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

More information about the database used: 

KyGovMaps Open Data Portal
https://opengisdata.ky.gov/datasets/ky-recreational-trails-wgs84wm/api?layer=6

Note: JSON file was downloaded and converted to CSV file to be used in this project. 

This project was written in Visual Studio Code and then later adopted to be also used in Jupyter notebook. The following packages were imported in this project: 

flask, folium, pandas, waitress, dash, matblotlib, plotly, numpy, webbrowser

How to run this project: 

1. Start with .ipynb file "KentuckyTrails".
2. You must install jupyter labs to run the code in the jupyter notebook (visit https://jupyterlabs.org/install) or run jupyter notebooks in a browser.
3. Once in the jupyter notebook, navigate to the directory where you downloaded the project files. (You should see the KentuckyTrails.ipynb file  needed to run this project).
4. Open the .ipynb file.
5. You may need to install the above-mentioned packages. Open terminal and run the following commands to install each package:

(pip install folium),
(pip install flask),
(pip install pandas),
(pip install matplotlib),
(pip install dash),
(pip install plotly),
(pip install numpy),
(pip install webbrowser),

6. Go back to the jupyter notebooks. You see we are now importing these packages. So you should be able to run the code now.
7. Select "Kernel" (top ribbon) and restart and run all cells one by one making sure that you turns stop Kernel between each run.

For visual studio (VS) Code users on Windows, make sure you get the python and Jupyter extensions.
