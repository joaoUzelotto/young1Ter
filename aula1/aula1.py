
while True:
 salario = int(input("DIGITE O SEU SALÁRIO: "))

 if salario <= 1200:
    print("estagiário")
 elif salario <= 2000:
    print("júnior")
 elif salario <= 4500:
    print("pleno")
 elif salario >= 5000:
    print("sênior")
 else:
    print("n entendi!")