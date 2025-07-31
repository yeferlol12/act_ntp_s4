n=int(input("Ingrese un número: "))
pares=0
impares=0
for numero in range(0, n ):
    if numero %2==0:
        pares+=1
    else:
        impares+=1
print("Cantidad de números pares: ", pares)
print("Cantidad de números impares: ", impares)

    

