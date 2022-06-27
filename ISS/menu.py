from os import system
import os

def menu():
    print('\n##########################')
    print('#    Menu de control de Orientacion de Antena   #')
    print('##########################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Giro manual de la antena.")
    print("2. Seguimiento de la ISS.")
    print("3. Posicion y Trayectoria de la ISS.")
    print("4. Salir.\n")

while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")



    if opc == '1':
        print("Ingrese direccion de giro (derecha, Izquierda )")
        direccion = str(input("Direccion: "))
        grados =  int(input("Ingrese grados: "))
        print('=================================================================================')
        print("Giro manual de la antena.s")
        print("\npython Control_manual.py \n")
        #system(f"python Prueba_1.py 1 {grados} {direccion}" )
        print('=================================================================================')


    elif opc == '2':
        print('=================================================================================')
        print("Seguimiento de la ISS.")
        print("\npython seguimiento.py \n")
        #system(f"sudo docker ps -a")
        print('=================================================================================')
    
    
    elif opc == '3':
        print('=================================================================================')
        print("Posicion y Trayectoria de la ISS")
        print("\npython seguimiento.py \n")
        system(f"python3 iss1.py" )
        print('=================================================================================')

    elif opc == '4':
        print('===================')
        print("||   Saliendo.   ||")
        print('===================')
        break


    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")