import urllib.request as url
import json
import math 
from cmath import sqrt

def estacion():
    ISS = url.Request("http://api.open-notify.org/iss-now.json")
    response_ISS = url.urlopen(ISS)
    ISS_obj = json.loads(response_ISS.read())
    dato3 = ISS_obj['iss_position']['latitude'];
    dato4 = ISS_obj['iss_position']['longitude'];
    print('Latitud', dato3)
    print('Longitud', dato4)

def separacion():
    try:        
        lat1 = float(input("Ingrese la latitud de su posición actual: "))
        lon1 = float(input("Ingrese la longitud de su posición actual: "))
        lat2 = float(input("Ingrese la latitud de la estación espacial: "))
        lon2 = float(input("Ingrese la longitud de la estación espacial: "))
    except ValueError:
        print("debes ingresar los valores correctos")

    rad = math.pi/180
    dlat = lat2-lat1
    dlon = lon2-lon1
    r = 6372.795477598

    a = math.sin(rad*dlat/2)**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2
    distancia = 2*r*math.asin(math.sqrt(a))
    print("la distancia es de ",distancia," Km")

def Menu():
    correcto = False
    num = 0
    while(not correcto):
        try: 
            correcto = True
            num = int(input("Ingrese una opción: "))
        except ValueError:
            print("Seleccione una opción valida")
    return num
salir = False 
while not salir:
    print("\n1 para latitud y longitud de la ISS \n2 para la distancia que hay de un punto a otro \n3 para deterner el programa")
    opcion = Menu()
    if opcion ==1:
        estacion()
        break
    elif opcion == 2:
        separacion()
    elif opcion == 3:
        salir = True
    else:
        print("\nIngrese una opción valida")
    