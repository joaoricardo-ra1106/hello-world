import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def conectar():
    try:
        conexao = mysql.connector.connect(
            host='localhost',      # ou '127.0.0.1'
            user='imc',    # substitua pelo seu usuário do banco
            password='imc@123',  # substitua pela sua senha
            database='JOAORICARDO'   # substitua pelo nome do banco
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def inserir_pessoa(conexao, nome, idade, altura, peso, classificacao):
    try:
        cursor = conexao.cursor()
        sql = """
        INSERT INTO imc (nome, idade, altura, peso, classificacao)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (nome, idade, altura, peso, classificacao)
        cursor.execute(sql, valores)
        conexao.commit()
        print("Registro inserido com sucesso!")
    except Error as e:
        print(f"Erro ao inserir: {e}")
    finally:
        cursor.close()

def buscar_nome(conexao, nome):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM imc WHERE nome LIKE %s"
        valor = f"%{nome}%"
        cursor.execute(sql, (valor,))
        resultados = cursor.fetchall()

        if resultados:
            headers = ["ID", "Nome", "Idade", "Altura", "Peso", "Classificação", "Criado Em", "Atualizado Em"]
            print("\nRegistros encontrados:\n")
            print(tabulate(resultados, headers=headers, tablefmt="grid"))
        else:
            print("Nenhum registro encontrado com esse nome.")
    except Error as e:
        print(f"Erro ao buscar: {e}")
    finally:
        cursor.close()

def atualizar_campo(conexao, id_pessoa, campo, novo_valor):
    try:
        cursor = conexao.cursor()
        sql = f"UPDATE imc SET {campo} = %s WHERE id = %s"
        valores = (novo_valor, id_pessoa)
        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Registro com id {id_pessoa} atualizado com sucesso.")
        else:
            print(f"Nenhum registro encontrado com id {id_pessoa}.")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
    finally:
        cursor.close()

def deletar_por_id(conexao, id_pessoa):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM imc WHERE id = %s"
        cursor.execute(sql, (id_pessoa,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Registro com id {id_pessoa} deletado com sucesso.")
        else:
            print(f"Nenhum registro encontrado com id {id_pessoa}.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")
    finally:
        cursor.close()

