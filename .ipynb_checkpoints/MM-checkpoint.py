import pandas as pd
import numpy as np
import re
import os
#import chart_studio.plotly as py #replaced by plotly.plotly as is deprecated according to some shit
import plotly_express as px
import plotly.graph_objs as go
import math
import plotly as py

#Route
DataFile=os.getcwd() + "/Data/MissingMigrants-Global-2019-03-29T18-36-07.csv"

#Read data
MM=pd.read_csv(filepath_or_buffer="/home/tobal/GithubProjects/MissingMigrants/Data/MissingMigrants-Global-2019-03-29T18-36-07.csv")
MM.head()


#Extract latitude and longitude into two columns
Lat=[]
Lon=[]
for i in range(MM.shape[0]):
    if type(MM["Location Coordinates"][i])==str:        
        Lat.append(float(re.sub(",", "", MM["Location Coordinates"][i].split()[0], count=1)))
        Lon.append(float(MM["Location Coordinates"][i].split()[1]))    
    else:
        Lat.append(float("nan"))
        Lon.append(float("nan"))
pass

#Add columns to original dataframe
MM["Lat"]=Lat
MM["Lon"]=Lon

#There is only one nan value, so we will delete it
sum(np.isnan(MM["Lat"]),0)
MM=MM[~np.isnan(MM["Lat"])]

#Plot based on coordinates
GOLatLon=go.Figure()
GOLatLon=GOLatLon.add_trace(go.Scattergeo(
        lon=MM["Lon"],
        lat=MM["Lat"],
        mode="markers"
        ))
GOLatLon.show()
#Use size of dead and missing as marker size and as color as well
GOLatLonSize=px.scatter_geo(data_frame=MM, lat="Lat", lon="Lon", size="Total Dead and Missing", color="Total Dead and Missing")
GOLatLonSize.show()

