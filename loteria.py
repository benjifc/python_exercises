#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, random           

menu_estado = True
numero_ganador = random.sample(range(0,10), 5)
def menu():
        os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo  
        msg = """
        ********************************************************************************
        *                      Bienvenidos al juego de la loteria                      *
        ********************************************************************************
        *                                                                              *
        *               1) Jugar                                                       *
        *               2) Salir                                                       *
        *                                                                              *
        ********************************************************************************
        """
        print(msg) 

def pausa():
    try:
        input("Pulse una tecla para continuar\n")
    except SyntaxError:
        pass

def ObtenerNumeros():
    Nums = []

    for x in range(5):
        numeros = int(input("Introduce un numero entre el 0 y el 9 => "))
        if 0 <= numeros <= 9:
            Nums.append(numeros)
        else:
            print("Numero erroneo.")
            pausa()
            numeros = int(input("Introduce un numero entre el 0 y el 9 => "))
            Nums.append(numeros)

    return Nums

def eresGanador(cupon):
    
    if cupon == numero_ganador:
        print ("\nFelicidades has GANADO!\n")
        print ("tu numero es: ", cupon, "\n")
        print ("Y el numero premiado es: ", numero_ganador, "\n")
    else:

        print ("\nHas perdido oooooo \n")
        print ("tu numero es:  ", cupon, "\n")
        print ("Y el numero premiado es: ", numero_ganador, "\n")
    pausa()

def Jugar():
    os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
    cupon = ObtenerNumeros()
    os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
    eresGanador(cupon)

        
while menu_estado:
    menu()
    opcion= input("\nIntroduzca su opcion [1-2]: ")
    if opcion == 1:        # Opcion Jugar
        print (20 * "*")
        print ("A Jugar ... !")
        print (20 * "*")
        Jugar()
        numero_ganador = random.sample(range(0,10), 5)


    elif opcion == 2:       # Opcion para salir
        os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
        print ("\nAdios!\n")
        menu_estado = False
    
    elif opcion == 3: # opcion oculta Hagamos fullerias
        print (numero_ganador)
        pausa()

        
    else:
        
        print("Opcion invalida\n")
        pausa()
