from defer import inline_callbacks
from IPython.display import Image
#import matplotlib

import requests
r = requests.get(url='http://api.open-notify.org/astros.json')
r.json()

import pandas as pd
import numpy as np

def translate_geo_to_pixels(longitude, latitude, max_x_px, max_y_px):
    scale_x = (((longitude +180)/360) * max_x_px)
    scale_y = (((latitude -90)/180) * max_y_px)

    return scale_x, scale_y
translate_geo_to_pixels(20,90,500,250)

def get_space_station_location():
    r = requests.get(url='http://api.open-notify.org/iss-now.json')
    space_station_location = (r.json())

    space_station_longitude = float(space_station_location['iss_position']['longitude'])
    print('space_station_longitude', space_station_longitude)

    space_station_latitude = float(space_station_location['iss_position']['latitude'])
    print('space_station_latitude', space_station_latitude)

    return(space_station_longitude, space_station_latitude)

from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
#%matplotlib inline 

get_space_station_location()

plt.figure(figsize = (20, 14))
 
m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=8)
m.drawmapboundary(fill_color='Black', linewidth =0)
m.fillcontinents(color = 'white', alpha =0.3)
m.drawcoastlines(linewidth=1, color='black')

space_station_longitude, space_station_latitude = get_space_station_location()
m.scatter(space_station_longitude, space_station_latitude, s=200, alpha=0.9, color='red')
