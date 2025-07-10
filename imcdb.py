from myFunctions.ler_float import ler_float
from myFunctions.ler_nome import ler_nome
from myFunctions.database import conectar, inserir_pessoa, buscar_nome, atualizar_campo, deletar_por_id

acao = input("Escolha uma ação: (i)nserir, (a)tualizar, (d)eletar, (b)uscar: ")

if acao == "i":
    peso = ler_float("Digite seu peso em kg: ", valorMinimo=30, valorMaximo=200)
    altura = ler_float("Digite sua altura em metros: ", valorMinimo=1, valorMaximo=2.5)
    idade = int(ler_float("Digite sua idade: ", valorMinimo=6, valorMaximo=100))
    nome = ler_nome("Digite seu nome: ")
    imc = peso / (altura ** 2)
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
    conexao = conectar()
    if conexao:
        inserir_pessoa(conexao, nome, idade, altura, peso, classificacao)
        conexao.close()


elif acao == "a":
    id = input("Digite o id que você quer atualizar: ")
    campo = input("Qual campo você quer atualizar (n)ome, (i)dade, (a)ltura (p)eso: ")
    novoValor = input("Digite o Novo Valor: ")
    conexao = conectar()
    if campo == "n":
        atualizar_campo(conexao, id, "nome", novoValor)
    elif campo == "i":
        atualizar_campo(conexao, id, "idade", novoValor)
    elif campo == "a":
        atualizar_campo(conexao, id, "altura", novoValor)
    elif campo == "p":
        atualizar_campo(conexao, id, "peso", novoValor)
    else: print(f"o campo {campo} esta errado, Porfavor Digite Um Valor Valido")

elif acao == "d":
    idParaDeletar = input("Digite o ID de um registro para Deletar: ")
    conexao = conectar()
    if conexao:
        deletar_por_id(conexao, idParaDeletar)


elif acao == "b":
    nome = input("Digite o nome a ser buscado: ")
    conexao = conectar()
    if conexao:
        buscar_nome(conexao, nome)

else:
    print(f"A ação {acao} é inválida")

