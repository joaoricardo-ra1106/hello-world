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

# Lista para armazenar os dados de todas as pessoas
pessoas = []

while True:
    # Entrada de dados
    peso = ler_float("Digite seu peso em kg: ", valorMinimo=30, valorMaximo=200)
    altura = ler_float("Digite sua altura em metros: ", valorMinimo=1, valorMaximo=2.5)
    idade = int(ler_float("Digite sua idade: ", valorMinimo=6, valorMaximo=100))
    nome = ler_nome("Digite seu nome: ")

    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau 1"
    elif imc < 40:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3 (mórbida)"

    # Armazena os dados da pessoa em um dicionário
    pessoa = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

    pessoas.append(pessoa)

    # Pergunta se deseja continuar
    continuar = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Exibe os dados de todas as pessoas
print("\n===== DADOS COLETADOS =====")
maiorPeso = 0
menorPeso = 200
MaiorIdade = 0
MenorIdade = 200
MaisAlto = 0
MenosAlto = 200
pessoaComMaiorPeso = {}
pessoaComMenorPeso = {}
PessoaMaisVelha = {}
PessoaMaisNova = {}
pessoaMaisAlta = {}
PessoaMenosAlta = {}

for i, pessoa in enumerate(pessoas, start=1):
    if maiorPeso < pessoa['peso']:
        maiorPeso = pessoa['peso']
        pessoaComMaiorPeso = pessoa
    if menorPeso > pessoa['peso']:
        menorPeso = pessoa['peso']
        pessoaComMenorPeso = pessoa
    if MaiorIdade < pessoa['idade']:
        MaiorIdade = pessoa ['idade']
        PessoaMaisVelha = pessoa
    if MenorIdade > pessoa['idade']:
        MenorIdade = pessoa['idade']
        PessoaMaisNova = pessoa
    if MaisAlto < pessoa['altura']:
        MaisAlto = pessoa['altura']
        pessoaMaisAlta = pessoa
    if MenosAlto > pessoa['altura']:
        MenosAlto = pessoa['altura']
        PessoaMenosAlta = pessoa
    #print(f"\nPessoa {i}:")
    #print(f"Nome: {pessoa['nome']}")
    #print(f"Idade: {pessoa['idade']} anos")
    #print(f"Peso: {pessoa['peso']} kg")
    #print(f"Altura: {pessoa['altura']} m")
    #print(f"IMC: {pessoa['imc']}")
    #print(f"Classificação: {pessoa['classificacao']}")

print(f"a pessoa {pessoaComMaiorPeso['nome']} tem {maiorPeso} kg que e o maior de todos(a)")
print(f"a pessoa {pessoaComMenorPeso['nome']} tem {menorPeso} kg que e o menor de todos(a)")
print(f"a pessoa {PessoaMaisVelha['nome']} tem {MaiorIdade} anos e mais velho(a)")
print(f"a pessoa {PessoaMaisNova['nome']} tem {MenorIdade} anos e mais novo(a)")
print(f"a pessoa {pessoaMaisAlta['nome']} tem {MaisAlto} de altura e mais alto de todos(a)")
print(f"a pessoa {PessoaMenosAlta['nome']} tem {MenosAlto} de altura e o menor de todos(a)")