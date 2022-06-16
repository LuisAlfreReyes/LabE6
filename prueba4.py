
#import requests
#import folium
#import requests
#import json

#def iss():

#    respuesta1 = requests.get("http://api.open-notify.org/iss-now.json")
#    contenido1 = json.loads(respuesta1.text)
#    latitud =(contenido1['iss_position']['latitude'])
#    longitud =(contenido1['iss_position']['longitude'])
#    m = folium.Map(location=[24.307883,11.610025],zoom_start=2)
#    tooltip = 'Haga click para más información'
#    folium.Marker([latitud,longitud],
#                    popup='<strong>Esta es la ISS</strong>',
#                    tooltip=tooltip,
#                    icon=folium.Icon(color='red',icon='plane')).add_to(m)
#    m.save('mundof.html')


import ISS_Info
import turtle
import time

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

while True:
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    print("Position: \n latitude: {}, longitude: {}".format(lat,lon))
    iss.goto(float(lon),float(lat))
    time.sleep(5)