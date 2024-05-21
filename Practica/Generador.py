def generador_pares(maximo):
    numero = 0
    while numero < maximo:
        yield numero
        numero += 2


generador = generador_pares(10)


for num in generador:
    print(num)
