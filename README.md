# Python Exercises
## 1) EJERCICIO CUADRADO DE SUMAS

Cree una función que te pida por pantalla dos números positivos y muestre por pantalla el cuadrado de la suma de los números que hay entre esos dos números inclusives. Tienes que controlar que el primer número siempre sea menor que el segundo, sino se mostrará por pantalla un mensaje de error. 

Ejemplo: def cuadrado_suma(1,3) -> El resultado debe ser el cálculo de aplicar (1+2+3)^2




## 2) LA LOTERÍA 

Cree una función la cual pida por pantalla 5 números y valide si esos 5 números corresponden al resultado del sorteo, mostrando por pantalla "Convinación Ganadora" ó "Convinación No Ganadora", seguido del resultado que tuvo el sorteo, por ejemplo: "Gracias por participar, el resultado del sorteo fue el 20,30,43,21,4". 
Para saber los números del sorteo, antes de pedir por pantalla los 5 números al usuario, tendrás que generar de manera aleatoria 5 números y guardarlo en una variable o array los cuales comprobarás con respecto a los que introducirá el usuario.


## 3) Log


Partiendo del siguiente registro de LOG que estará guardado en un fichero llamado log.txt

213.25.23.24;01/03/2017;200MB;Sevilla
32.45.288.12;01/03/2017;70MB;Madrid
217.26.35.34;01/03/2017;20MB;Barcelona
32.45.288.12;01/03/2017;700MB;Madrid
213.25.23.24;01/03/2017;60MB;Sevilla
3.25.15.13.1;02/03/2017;300MB;Toledo
35.851.45.23;02/03/2017;2MB;Huelva
213.25.23.24;03/03/2017;150MB;Sevilla

Cree una función que tenga como parámetro de entrada el LOG y muestre por pantalla lo siguiente. 

Hay "X" IP's distintas en todo el LOG. 
El día "dd/mm/yyyy" la IP "X" se descargó "M" megas. (Mostrar por cada IP, ¡ojo! a IP iguales por día)
La ciudad que ha consumido mas megas en todo el LOG es: "C"


Para las tres salidas anteriores por pantallas habrá que recorrer todo el Log. 

Para recorrer el LOG se podría usar, por ejemplo:

file = open('log.txt','r') 
for line in file:
    print(line)
file.close()

Ejemplo: def tratar_log(ruta_file)


## 5) Parking

Cree una función que calcule el precio a pagar en un parking y lo muestre por pantalla. Tienes que saber que:

La media hora cuesta 3€ y la hora 6€.
Si se aparca menos de 2 horas se cobrará por hora o media hora. Es decir, si un coche lleva aparcado menos de 31 minutos se cobrará 3€  ....... si lleva entre 31 y 61 minutos se cobrará 6€ .... si lleva entre 61 y  91 minutos se cobrará 9€ ... si lleva entre 91 y 120  minutos se cobrará 12€.   
Si se aparca más de 2 horas, pero menos de 6 horas, se le cobrará un precio único de 30€. 
Si se aparca más de 6 horas pero menos de 24 horas, se le cobrará un precio único de 80€. 
Si se aparca por más de 24 horas saldrá un mensaje por pantalla: "Llamar a Grúa".

La función tendrá como entrada, la fecha y hora de entrada y de salida en formato dd/mm/aaaa hh:mm.

Ejemplo: def calcula_precio_parking(fecha_entrada,fecha_salida)

