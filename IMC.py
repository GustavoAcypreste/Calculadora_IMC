nome = input("Digite o seu nome: ")
idade = input("Digite sua idade em anos: ")
opcao = int(input("informe seu sexo: [1] masculino n/[2] feminino: "))
peso = input("Digite seu peso em kg: ")
altura = input("Digite a sua altura em metros: ")

print(nome, idade, sep=" ") 
imc = (float(peso)/ (float(altura) ** 2))
print(imc)

if opcao == 1:

    abaixoMasc = (float(imc) < 18)
    normalMasc = (float(imc) >= 18 and float(imc)< 25)
    acimaMasc = (float(imc) >= 25)

    if normalMasc:
        print("seu IMC está normal")

    if acimaMasc: 
       print("Seu IMC está acima do desejado")

    if abaixoMasc:
        print("seu IMC está abaixo do desejado")

elif opcao == 2:

    abaixofem = (float(imc) < 18.5)
    normalfem = (float(imc) >= 18.5 and float(imc)< 25)
    acimafem = (float(imc) >= 25)

    if normalfem:
        print("seu IMC está normal")

    if acimafem: 
        print("Seu IMC está acima do desejado")

    if abaixofem:
        print("seu IMC está abaixo do desejado")