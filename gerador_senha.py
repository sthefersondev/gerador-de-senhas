import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas ===")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada (ex: 12): "))
        senha = gerar_senha(tamanho)
        print(f"\nSua senha gerada é:\n{senha}")
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
