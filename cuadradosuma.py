#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os           
os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
msg = """
********************************************************************************
*           INTRODUZCA DOS NUMEROS PARA CALCULAR EL CUADRADO DE SUMA           *
********************************************************************************
"""
print(msg)                                                  #Mostrmos pantalla de adquisición de datos
print ("Introduzca el primer numero del intervalo: ")
a=input()
print ("Introduzca el segundo numero del intervalo: ")
b=input()



def verifica(funcion):                         # Creamos decorador con la restricciones
    def verificador(*args,**kwargs):
         if a<b:
            funcion(*args,**kwargs)
         else:
            print (str(a)+ " no es mayor que "+ str(b) + " no podemos hacer el calculo")
     
    return verificador

@verifica    # Invocamos decorador anteriormente definido
def cuadrado_suma(a,b):    # Funcion con el calculo del cuadrado de suma
     
        Numeros = range(a,b)
        suma=0

        for numero in Numeros:
            suma+=numero
        suma=suma**2
        print("El resultado es: "+str(suma))

cuadrado_suma(a,b) # invocamos la funcion




         
