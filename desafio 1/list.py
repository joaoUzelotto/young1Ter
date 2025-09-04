import random
while True:
 listas = int(input("DIGITE UM NÚMERO: "))

 lista = []

 while listas <= 16384:
    lista.append(listas)
    listas *= 2

 print("SUA LISTA: ", lista)
