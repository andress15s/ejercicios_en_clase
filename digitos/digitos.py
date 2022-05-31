

X = int(input("Digite el numero a evaluar: "))

D = 0
Z = X

while Z != 0:
    Z = Z // 10
    D = D + 1

print("-----------------------------------------")
print("El numero" , X , " tiene " , D , "Digitos")
print("-----------------------------------------")