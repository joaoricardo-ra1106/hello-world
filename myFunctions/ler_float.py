def ler_float(mensagem: str, valorMinimo: float = None, valorMaximo: float = None) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            if valorMinimo is not None and valorMaximo is not None:
                if valorMinimo <= valor <= valorMaximo:
                    return valor
                else:
                    print(f"❌ O valor deve estar entre {valorMinimo} e {valorMaximo}.")
            else:
                return valor
        except ValueError:
            print("❌ Entrada inválida. Digite um número válido (ex: 70.5).")