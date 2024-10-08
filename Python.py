numero = 1
while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print("CocaCola")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Cola")
    else:
        print(numero)
    numero += 1