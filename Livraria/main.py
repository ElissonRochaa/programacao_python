import json


def cadastrar_livro():
    livro = {}
    livro['titulo'] = input("Digite o Titulo do Livro: ")
    livro['autor'] = input("Digite o nome do Autor: ")
    livro['ano_publicacao'] = int(input("Digite o ano de publicação: "))
    livro['preco_venda'] = float(input("Digite o preço de venda: "))

    return livro


def menu():
    print("Menu:")
    print("1-Cadastrar Livro")
    print("2-Listar Livros")
    print("0-Sair")

def listar_livros():
    print("Listando..")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            livros = json.load(arquivo)
    except FileNotFoundError:
        livros = []
    finally:
        return livros

def salvar_arquivo(nome_arquivo, livros):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(livros, arquivo, indent=4)


def main():
    livros = ler_arquivo("livros.json")
    opcao = -1
    while opcao!=0: # Laco de repeticao
        try:
            menu()
            print()
            opcao = int(input("Digite a opção desejada: "))

        except ValueError as ve:
            print("Erro: ", ve)
        except Exception as e:
            print("Aconteceu algo inesperado: ", e)
        else:
            if opcao == 1: #Condicional
                livros.append(cadastrar_livro())
            elif opcao == 2:
                print("Listar Livros")
                print(livros)
            elif opcao == 0:
                print("Programa sendo encerrado...")
                salvar_arquivo("livros.json", livros)
            else:
                print("Opção invalida...")


if __name__ == "__main__":
    main()