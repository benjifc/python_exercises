#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Esta version no se ha usado Panda por requerimientos de enunciado 

from collections import defaultdict
import operator
import os           



### Clase Log No contiene metodos publicos se procesa todo en el constructor 

class Log():
    __Lineas=[]    
    __Ips=[]
    __Dias=[]
    __DiasVsIps=[]
    __Ciudades=[]
    def __init__(self,archivo = str("log.txt")):
           self.__archivo = archivo
           file = open(self.__archivo,'r') 
           for line in file:
                self.__Lineas.append(line.strip('\n').split(';'))
           file.close()
           self.__FIps()
           self.__FDias()
           self.__FCiudades()
           self.__FDiasVsIps()
           self.__ConsumoVsCiudad()
           


    def __FIps(self):                                                              ### Distinct de IPS
        for item in self.__Lineas:
            self.__Ips.append(item[0])
        self.__Ips= set(self.__Ips)
        print("Hay " + str(len(self.__Ips)) +  " IP's distintas en todo el LOG.")
       

    def __FDiasVsIps(self):                                                       ### Listado de  Dias, ips, megas
       olog = defaultdict(list)             
       for D in self.__Dias:
            ilog = defaultdict(int) 
            for item in self.__Lineas:
                if item[1] == D:
                        ilog[str(item[0])] += int(item[2].replace('MB',''))

            olog[str(D)].append(ilog.items())
       for D in self.__Dias:
           for il in olog[D]:
                  print(" El día "+str(D)+" la IP "+str(il[0][0])+" se descargó "+str(il[0][1])+" megas.")
      
    def __ConsumoVsCiudad(self):                                                ### Ciudad con Mayor Consumo de megas
         clog = defaultdict(int) 
         for item in self.__Lineas:
            clog[str(item[3])] += int(item[2].replace('MB',''))
         ciudad = max(clog.iteritems(), key=operator.itemgetter(1))[0]
         print("La ciudad que ha consumido mas megas en todo el LOG es: "+str(ciudad))


    def __FCiudades(self):                                                        ### Distinct Ciudades
        
        for item in self.__Lineas:
            self.__Ciudades.append(item[3])
        self.__Ciudades= set(self.__Ciudades)
       
    def __FDias(self):                                                            ### Distinct Dias
        for item in self.__Lineas:
               self.__Dias.append(item[1])
        self.__Dias= set(self.__Dias)
        
     

#######################################################################################

#                             INICIO PROGRAMA                                         #


#######################################################################################


os.system('clear')  # Limpio pantalla haciendo una llamada al sistema operativo
msg = """
********************************************************************************
*                              Visualizador de Log                             *
********************************************************************************
"""
print(msg)   


def tratar_log(ruta_file):
    obj = Log(ruta_file)

tratar_log('log.txt')