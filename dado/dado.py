#dado
import random

#input

numero = int(input("Digite el numero de veces quw desea lanzar el dado : "))

#procesing

cara_3= "3 : "


if numero>0: 
  while numero>0:
    dado=random . randint(1,6)
    numero=numero-1
    if dado==3:
      cara_3=cara_3+ "*"
   

else:
  print("el numero de lanzamientos no es valido")

#output
print("el numero de veces que salio la cara 3 es:" + str (cara_3))