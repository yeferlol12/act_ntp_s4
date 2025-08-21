def numeros_pares(lista):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares
numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = numeros_pares(numeros)

print("Números pares:", resultado)
    

