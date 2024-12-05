import hashlib


def main():
    while True:
        entrada = input(
            "Digite uma frase para gerar o hash (ou 'sair' para encerrar): ")

        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break

        mascara = hashlib.sha1(entrada.encode())

        print(
            f"Hash SHA-1 da frase '{entrada}': {mascara.hexdigest()}")


if __name__ == "__main__":
    main()
