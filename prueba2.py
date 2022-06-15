import urllib.request as url
import json
import folium

ISS = url.Request("http://api.open-notify.org/iss-now.json")
response_ISS = url.urlopen(ISS)

ISS_obj = json.loads(response_ISS.read())

print(ISS_obj['iss_position']['latitude'])
print(ISS_obj['iss_position']['longitude'])

long = ISS_obj['iss_position']['longitude']
lat = ISS_obj['iss_position']['latitude']

m = folium.Map(location=[lat,long],zoom_start=2,tiles='Stamen Terrain')
icon=folium.Icon(color="red")
folium.Marker([lat,long], tooltip="ISS", icon=icon).add_to(m)
m