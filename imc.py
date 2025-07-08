from myFunctions.ler_float import ler_float

def ler_nome(mensagem: str) -> str:
    while True:
        nome = input(mensagem).strip()
        if not nome:
            print("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            print("O nome não pode conter números.")
        else:
            return nome



# Entrada de dados

peso = ler_float("Digite seu peso em kg: ", valorMinimo=30, valorMaximo=200)
altura = ler_float("Digite sua altura em metros: ", valorMinimo=1, valorMaximo=2.5)
idade = int(ler_float("Digite Sua Idade:", valorMinimo=6, valorMaximo=100))
nome = ler_nome("Digite Seu Nome:")

print(f"Sua idade e: {idade}")
print(f"seu nome  e: {nome}")

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
elif imc < 35:
    print("Classificação: Obesidade grau 1")
elif imc < 40:
    print("Classificação: Obesidade grau 2")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")
