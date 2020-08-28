menu = """
Bienvenido al conversor de monedas📊🗳

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opción : """

opcion = int(input (menu))
if opcion == 1 :
    pesos = input("¿cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3768
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion ==2:
    pesos = input("¿cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 73.88
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 22.09
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else: 
    print('Ingrese uan opción correcta por favor')




dolares1 = input("¿Cuántos dolares estadounidenses tienes?: ")
dolares1 = float(dolares1)
pesos1 = dolares1 * valor_dolar
pesos1 = round(pesos1, 2)
pesos1 = str(pesos1)
print("Tines $ " + pesos1 +" pesos colombianos")