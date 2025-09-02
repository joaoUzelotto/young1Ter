
escolha = int(input("Qual classificação de filme deseja? (1- L 2- 10 3- 12 4- 14 5- 16 6- 18)"))
idade = int(input("Qual sua idade? "))



if escolha == 1 and idade >= 7:
    print("Você pode assistir ao filme!")
elif escolha == 1 and idade < 7:
    print("Você só pode assistir com os pais!")

elif escolha == 2 and idade >= 10:
    print("Você pode assistir ao filme!")
elif escolha == 2 and idade <= 7:
    print("Você só pode assistir com os pais!")
elif escolha == 3 and idade >= 12:
    print("Você pode assistir ao filme!")
elif escolha == 3 and idade <= 9:
    print("Você só pode assistir com os pais!")

else:
    print("Não entendi! vc é cego e não vê as opções!")

