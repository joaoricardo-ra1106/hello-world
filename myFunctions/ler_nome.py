def ler_nome(mensagem: str) -> str:
    while True:
        nome = input(mensagem).strip()
        if not nome:
            print("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            print("O nome não pode conter números.")
        else:
            return nome