"""
Calculadora de terminal
Projeto simples em Python para praticar input, operadores, funções e laços.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero"
    return a / b


def ler_numero(mensagem):
    """Pede um número ao usuário e repete até ele digitar um valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def main():
    operacoes = {
        "1": ("+", somar),
        "2": ("-", subtrair),
        "3": ("x", multiplicar),
        "4": ("/", dividir),
    }

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "0":
            print("Até a próxima!")
            break

        if escolha not in operacoes:
            print("Opção inválida, tente novamente.")
            continue

        simbolo, funcao = operacoes[escolha]
        n1 = ler_numero("Primeiro número: ")
        n2 = ler_numero("Segundo número: ")
        resultado = funcao(n1, n2)
        print(f"\n{n1} {simbolo} {n2} = {resultado}")


if __name__ == "__main__":
    main()
