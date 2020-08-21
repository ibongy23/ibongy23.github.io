pesos = input("¿cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3768
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")

dolares1 = input("¿Cuántos dolares estadounidenses tienes?: ")
dolares1 = float(dolares1)
pesos1 = dolares1 * valor_dolar
pesos1 = round(pesos1, 2)
pesos1 = str(pesos1)
print("Tines $ " + pesos1 +" pesos colombianos")