#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, datetime, re,  pytz
from dateutil.tz import tzlocal


menu_estado = True

def menu():
        os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo  
        msg = """
        ********************************************************************************
        *                      Bienvenidos al Parcking                                 *
        ********************************************************************************
        *                                                                              *
        *               1) Pagar                                                       *
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

def ObtenerFechas():
  Fechas = []
  pattern = re.compile(r"\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}")
  I=0
  for x in range(2):
        strFecha=""
        if(x%2!=0):
            strFecha =" salida "
        else:
            strFecha =" entrada "
        I+=1 
        fecha = raw_input("Introduce las fechas de " + strFecha + " => ")
        if pattern.match(fecha):
            Fechas.append(fecha)
        else:
            print("Fecha erronea. escribala en este formato dd/mm/aaaa hh:mm por favor.")
            pausa()
            fecha = raw_input("Introduce la fecha de " + strFecha + " de nuevo => ")
            Fechas.append(fecha)

  return Fechas

def calcula_precio_parking(fecha_entrada,fecha_salida):
         Minutos = (fecha_salida - fecha_entrada).seconds / 60
         Dias = (fecha_salida - fecha_entrada).days
       
         if fecha_salida < fecha_entrada:
               os.system('clear') 
               print("Vuelve al DeLorean Marty McFly")
               print """
             __---~~~~--__                      __--~~~~---__
            `\---~~~~~~~~\\                    //~~~~~~~~---/'  
              \/~~~~~~~~~\||                  ||/~~~~~~~~~\/ 
                          `\\                //'
                            `\\            //'
                              ||          ||      Hey Doc! La fecha de salida NO PUEDE SER MENOR a la de entrada ...
                    ______--~~~~~~~~~~~~~~~~~~--______              
               ___ // _-~                        ~-_ \\ ___  
              `\__)\/~                              ~\/(__/'          
               _--`-___                            ___-'--_        
             /~     `\ ~~~~~~~~------------~~~~~~~~ /'     ~\        
            /|        `\                          /'        |\     
           | `\   ______`\_         DMC        _/'______   /' |          
           |   `\_~-_____\ ~-________________-~ /_____-~_/'   |  
           `.     ~-__________________________________-~     .'       
            `.      [_______/------|~~|------\_______]      .'
             `\--___((____)(________\/________)(____))___--/'           
              |>>>>>>||                            ||<<<<<<|
              `\<<<<</'                            `\>>>>>/' 
                """
               pausa()
               pagar()
                        
         if Dias < 0 :
            if Minutos <= 30:
                print("Tiene que pagar 3€")
            elif Minutos > 30 and Minutos <=60:
                print("Tiene que pagar 6€")
            elif Minutos > 60 and Minutos <=90:
                print("Tiene que pagar 9€")
            elif Minutos > 90 and Minutos <=120:
                print("Tiene que pagar 12€")
            elif Minutos > 120 and Minutos <=360:
                print("Tiene que pagar 30€")
            elif Minutos > 360 and Minutos <=1440:
                print("Tiene que pagar 80€")
            else:
                print("Llamar a Grúa")
         else:
             print("Llamar a Grúa")
             
         

def pagar():
    fechas = ObtenerFechas()
    tz = pytz.timezone('Europe/Madrid')
    inicio = tz.localize(datetime.datetime.strptime(fechas[0],'%d/%m/%Y %H:%M'))
    fin = tz.localize(datetime.datetime.strptime(fechas[1],'%d/%m/%Y %H:%M'))
    calcula_precio_parking(inicio,fin)
    pausa()

while menu_estado:
    pattern = re.compile(r"\d{1}")
    menu()
    opcion= raw_input("\nIntroduzca su opcion [1-2]: ")
    if pattern.match(opcion):
        
        if int(opcion) == 1:        # Opcion pagar
            print (20 * "*")
            print ("A Pagar ... !")
            print (20 * "*")
            pagar()
        
            


        elif int(opcion) == 2:       # Opcion para salir
            os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
            print ("\nAdios!\n")
            menu_estado = False
        
            
        else:
            
            print("Opcion invalida\n")
            pausa()

        