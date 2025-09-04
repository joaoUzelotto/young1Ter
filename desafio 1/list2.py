
lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

for i in range(10):
    lista[i], lista[19 - i] = lista[19 - i], lista[i]

for i in range(20):
    print(f"N[{i}] = {lista[i]}")