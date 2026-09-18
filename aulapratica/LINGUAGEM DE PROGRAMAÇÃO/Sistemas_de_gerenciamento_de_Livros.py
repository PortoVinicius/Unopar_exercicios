import matplotlib.pyplot as plt


# Passo 1: Definir a classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | " \
               f"Gênero: {self.genero} | Quantidade: {self.quantidade}"


# Passo 2: Criar a lista de livros
livros = []


# Passo 3: Função para cadastrar um novo livro
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor: ")
    genero = input("Digite o gênero: ")
    quantidade = int(input("Digite a quantidade disponível: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)

    print("\nLivro cadastrado com sucesso!")


# Função para listar todos os livros
def listar_livros():
    if len(livros) == 0:
        print("\nNenhum livro cadastrado.")
        return

    print("\n===== LIVROS CADASTRADOS =====")

    for livro in livros:
        print(livro)


# Função para buscar um livro pelo título
def buscar_livro():
    titulo_busca = input("Digite o título que deseja buscar: ")

    encontrado = False

    for livro in livros:
        if livro.titulo.lower() == titulo_busca.lower():
            print("\nLivro encontrado:")
            print(livro)
            encontrado = True
            break

    if not encontrado:
        print("\nLivro não encontrado.")


# Passo 4: Gerar gráfico por gênero
def gerar_grafico():
    if len(livros) == 0:
        print("\nNão há livros cadastrados para gerar o gráfico.")
        return

    generos = {}

    for livro in livros:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    plt.bar(generos.keys(), generos.values())

    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de livros")

    plt.show()


# Menu principal
while True:
    print("\n===== SISTEMA DA BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Gerar gráfico por gênero")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        buscar_livro()

    elif opcao == "4":
        gerar_grafico()

    elif opcao == "5":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!")
