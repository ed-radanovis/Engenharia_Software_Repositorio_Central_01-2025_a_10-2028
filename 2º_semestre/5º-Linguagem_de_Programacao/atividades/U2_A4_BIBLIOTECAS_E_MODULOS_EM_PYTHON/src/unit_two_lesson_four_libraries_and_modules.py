# -*- coding: utf-8 -*-
# Sistema de Gerenciamento de Livros para Biblioteca
# Utilizando classes, funções e a biblioteca matplotlib para gráficos

import matplotlib.pyplot as plt

class Livro:
    """
    Classe que representa um livro na biblioteca.
    Atributos: título, autor, gênero e quantidade disponível.
    """
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
    
    def __str__(self):
        """Retorna uma representação em string do livro"""
        return f"'{self.titulo}' por {self.autor} | Gênero: {self.genero} | Disponível: {self.quantidade}"

# Lista para armazenar os livros
biblioteca = []

def cadastrar_livro():
    """
    Função para cadastrar um novo livro na biblioteca.
    Solicita os dados do livro ao usuário e adiciona à lista.
    """
    print("\n" + "="*50)
    print("CADASTRO DE NOVO LIVRO")
    print("="*50)
    
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    genero = input("Digite o gênero do livro: ").strip()
    
    # Validação da quantidade
    while True:
        try:
            quantidade = int(input("Digite a quantidade disponível: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Cria o objeto Livro e adiciona à biblioteca
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"\n✅ Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    """
    Função para listar todos os livros cadastrados na biblioteca.
    """
    print("\n" + "="*50)
    print("LISTA DE TODOS OS LIVROS")
    print("="*50)
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    for i, livro in enumerate(biblioteca, 1):
        print(f"{i}. {livro}")

def buscar_livro_por_titulo():
    """
    Função para buscar um livro pelo título (busca parcial case-insensitive).
    """
    print("\n" + "="*50)
    print("BUSCA DE LIVRO POR TÍTULO")
    print("="*50)
    
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    termo_busca = input("Digite o título ou parte do título para buscar: ").strip().lower()
    
    livros_encontrados = []
    for livro in biblioteca:
        if termo_busca in livro.titulo.lower():
            livros_encontrados.append(livro)
    
    if livros_encontrados:
        print(f"\n📚 Livros encontrados com '{termo_busca}':")
        for i, livro in enumerate(livros_encontrados, 1):
            print(f"{i}. {livro}")
    else:
        print(f"\n❌ Nenhum livro encontrado com '{termo_busca}' no título.")

def gerar_grafico_generos():
    """
    Função para gerar um gráfico de barras com a quantidade de livros por gênero.
    Utiliza a biblioteca matplotlib para visualização.
    """
    print("\n" + "="*50)
    print("GRÁFICO DE LIVROS POR GÊNERO")
    print("="*50)
    
    if not biblioteca:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return
    
    # Contagem de livros por gênero
    contagem_generos = {}
    for livro in biblioteca:
        if livro.genero in contagem_generos:
            contagem_generos[livro.genero] += livro.quantidade
        else:
            contagem_generos[livro.genero] = livro.quantidade
    
    # Preparar dados para o gráfico
    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())
    
    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(generos, quantidades, color=["#722929", "#1D5855", "#181F20", "#9C7B03", "#5C5959", "#0B00AA"])
    plt.title('Quantidade de Livros por Gênero', fontsize=16, fontweight='bold')
    plt.xlabel('Gêneros', fontweight='bold')
    plt.ylabel('Quantidade de Livros', fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Adicionar valores nas barras
    for i, valor in enumerate(quantidades):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Gráfico gerado com sucesso!")

def menu_principal():
    """
    Função que exibe o menu principal e gerencia as opções do sistema.
    """
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
        print("="*50)
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico por gênero")
        print("5. Sair do sistema")
        print("="*50)
        
        opcao = input("Digite a opção desejada: ").strip()
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro_por_titulo()
        elif opcao == "4":
            gerar_grafico_generos()
        elif opcao == "5":
            print("Obrigado por usar o sistema! Até logo! 👋")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 5.")

# Execução principal do programa
if __name__ == "__main__":
    # Adicionar alguns livros de exemplo para teste
    biblioteca.append(Livro("Dom Casmurro", "Machado de Assis", "Romance", 5))
    biblioteca.append(Livro("O Cortiço", "Aluísio Azevedo", "Romance", 3))
    biblioteca.append(Livro("Iracema", "José de Alencar", "Romance", 4))
    biblioteca.append(Livro("O Alienista", "Machado de Assis", "Ficção", 2))
    biblioteca.append(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 6))
    biblioteca.append(Livro("1984", "George Orwell", "Ficção Científica", 3))
    biblioteca.append(Livro("A Revolução dos Bichos", "George Orwell", "Fábula", 4))
    biblioteca.append(Livro("Clean Code", "Robert Cecil Martin", "Tecnologia / Programação", 8))
    
    print("\n \n Bem-vindo ao Sistema de Gerenciamento de Biblioteca! 📚")
    print("\n \n Alguns livros de exemplo foram adicionados para teste.")
    menu_principal()