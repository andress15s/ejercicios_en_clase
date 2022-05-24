#dado
import random

#input

numero = int(input("Digite el numero de veces quw desea lanzar el dado : "))

#procesing
cara_1= "1 : "
cara_2= "2 : "
cara_3= "3 : "
cara_4= "4 : "
cara_5= "5 : "
cara_6= "6 : "

if numero>0: 
  while numero>0:
    dado=random . randint(1,6)
    numero=numero-1
    if dado==1:
      cara_1=cara_1+ "*"
    elif dado==2:
      cara_2=cara_2+ "*"
    elif dado==3:
      cara_3=cara_3+ "*"
    elif dado==4:
      cara_4=cara_4+ "*"
    elif dado==5:
      cara_5=cara_5+ "*"
    elif dado==6:
      cara_6=cara_6+ "*"

else:
  print("el numero de lanzamientos no es valido")

#output

print("el numero de veces que salio la cara 1 es:" + str (cara_1))

print("el numero de veces que salio la cara 2 es:" + str (cara_2))

print("el numero de veces que salio la cara 3 es:" + str (cara_3))

print("el numero de veces que salio la cara 4 es:" + str (cara_4))

print("el numero de veces que salio la cara 5 es:" + str (cara_5))

print("el numero de veces que salio la cara 6 es:" + str (cara_6))