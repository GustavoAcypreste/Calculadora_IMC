nome = input("Digite o seu nome: ")
idade = input("Digite sua idade em anos: ")
peso = input("Digite seu peso em kg: ")
altura = input("Digite a sua altura em metros: ")

print(nome, idade, sep=" ")
imc = (float(peso)/ (float(altura) ** 2))
print(imc)

abaixo = (float(imc) < 18)
normal = (float(imc) >= 18 and float(imc)< 25)
acima = (float(imc) >= 25)

if normal:
    print("seu IMC está normal")

if acima: 
    print("Seu IMC está acima do desejado")

if abaixo:
    print("seu IMC está abaixo do desejado")
