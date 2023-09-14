nome = input("Digite o seu nome: ")
idade = input("Digite sua idade em anos: ")
peso = input("Digite o seu peso em kg: ")
altura = input("Digite a sua altura em metros: ")

print(nome, idade, sep=" ")
imc = (float(peso)/ (float(altura) ** 2))
print(imc)
print(int(imc))