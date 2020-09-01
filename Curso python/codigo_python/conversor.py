def conversor (tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos peoso " + tipo_pesos + " tienes?")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes" + dolares "dólares")

menu = """
Bienvenido al conversor de monedas📊🗳

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opción : """

opcion = int(input (menu))
if opcion == 1 :
    conversor("colombianos", 3768)
elif opcion ==2:
    conversor("argentinos", 73.88)
elif opcion == 3:
    conversor("mexicanos", 22.09)
else: 
    print('Ingrese uan opción correcta por favor')




