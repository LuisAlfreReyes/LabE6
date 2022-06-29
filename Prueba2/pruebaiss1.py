import urllib.request as url
import json
import math 
import time
from datetime import datetime

from cmath import sqrt
##################################################################################################################################################################################
def estacion1():
    while True:
        try:
            ISS = url.Request("http://api.open-notify.org/iss-now.json")
            response_ISS = url.urlopen(ISS)
            ISS_obj = json.loads(response_ISS.read())
            dato3 = ISS_obj['iss_position']['latitude'];
            dato4 = ISS_obj['iss_position']['longitude'];
            latitud1 = 14.64433 #latitud de nuestro punto
            longitud1 = -90.51339 #longitud de nuestro punto
            lat2 = float(dato3) #latitud del satelite
            lon2 = float(dato4) #longitud del satelite
            rad = math.pi/180
            dlat = lat2-latitud1
            dlon = lon2-longitud1
            Rdt = 6372.795477598 #radio de la tierra en km
            a = math.sin(rad*dlat/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlon/2)**2 #datos dentro de la raíz
            distancia = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
            h = 408 #altura de la iss en km
            el = math.atan(h/distancia)
            sube = el*(180/math.pi)
            h = 1501.8
            medida = 2*h*Rdt+h**2
            horizonte = math.sqrt(medida)
            print("El horizonte es de: ", round(horizonte,2))
##################################################################################################################################################################################
            if(float(dato3) > latitud1 and float(dato4) > longitud1): #Cuadrante I; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LONGITUD
                dlatI = 0 
                dlonI = lon2-longitud1
                a = math.sin(rad*dlatI/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonI/2)**2 #datos dentro de la raíz
                distanciaI = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaI/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. Distancia en longitud: ", round(distanciaI,2),"km, I cuadrante")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ",round(90-giro,2) ,"en grados, a favor de las agujas del reloj \n")
            elif(float(dato3) > latitud1 and float(dato4) < longitud1): #Cuadrante II; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LATITUD
                dlatII = lat2-latitud1
                dlonII = 0 
                a = math.sin(rad*dlatII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonII/2)**2 #datos dentro de la raíz
                distanciaII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaII/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. Distancia en latitud: ", round(distanciaII,2), "km, II cuadrante")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ", round(90-giro,2) ,"en grados, en contra de las agujas del reloj \n")
            elif(float(dato3) < latitud1 and float(dato4) < longitud1): #Cuadrante III; longitud > -90.51327 ; Latitud > 14.64072-----DISTANCIA DE LONGITUD
                dlatIII = 0 
                dlonIII = lon2-longitud1
                a = math.sin(rad*dlatIII/2)**2 + math.cos(rad*latitud1)*math.cos(rad*latitud1)*math.sin(rad*dlonIII/2)**2 #datos dentro de la raíz
                distanciaIII = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaIII/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. longitud: ", round(distanciaIII,2),"km, cuadrante III")
                print("Angulo de elevación: ", round(sube,2),"Azimut: ", round(180-giro,2) ,"en grados, en contra de las agujas del reloj \n")
            elif(float(dato3) < latitud1 and float(dato4) > longitud1): #Cuadrante IV; longitud > -90.51327 ; Latitud > 14.64072------DISTANCIA DE LATITUD
                dlatIV = lat2-latitud1
                dlonIV = 0
                a = math.sin(rad*dlatIV/2)**2 + math.cos(rad*latitud1)*math.cos(rad*lat2)*math.sin(rad*dlonIV/2)**2 #datos dentro de la raíz
                distanciaIV = 2*Rdt*math.asin(math.sqrt(a)) #formula Haversine, distancia de nuestro punto a la proyección del satelite
                azimut = math.acos(distanciaIV/distancia)
                giro = azimut*(180/math.pi) 
                print("Distancia de origen a proyección del iss: ", round(distancia,2), "km. latitud: ", round(distanciaIV,2), "km, cuadrante IV")
                print("Angulo de elevación: ", round(sube,2)," Azimut: ", round(180-giro,2) ,"en grados, a favor de las agujas del reloj \n")
##################################################################################################################################################################################
            time.sleep(5)
        except Exception as e:
            print(str(e))
            break 
##################################################################################################################################################################################
def pasoiss():
    # Latitud y Logitud de la Ciudad de Madrid (usada como ejemplo)
    latitud=14.5833
    longitud=-90.5167
    n=10 #número de veces que pasará la ISS

    Pass=url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud,longitud,n))
    response_Pass= url.urlopen(Pass)

    Pass_obj = json.loads(response_Pass.read())
    print ("")
    pass_list=[]
    for count,item in enumerate(Pass_obj["response"], start=0):
        pass_list.append(Pass_obj['response'][count]['risetime'])
        print(datetime.fromtimestamp(pass_list[count]).strftime('%d-%m-%Y %H:%M:%S'))

##################################################################################################################################################################################
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
    print("\n1 El azimut y la elevación \n2 Para determinar la fecha que pasa la iss \n3 para deterner el programa")
    opcion = Menu()
    if opcion ==1:
        estacion1()
    elif opcion == 2:
        pasoiss()
    elif opcion == 3:
        salir = True
    else:
        print("\nIngrese una opción valida")
    