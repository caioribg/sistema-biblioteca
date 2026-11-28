from biblioteca import cadastrar_livro, lista_livros, pesquisar_por_id, pesquisar_por_titulo, atualizar_livro, excluir_livro

def menu():
    print("\n")
    print("=" * 60)
    print("\tSISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("=" * 60)

    print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

    while True:

        opc = int(input("\nSelecione uma opção: "))
        while opc < 0 or opc > 5:
            print("\nERRO: Informe uma opção entre 0 e 5.\nTente novamente.", end="\n")

            opc = int(input("Selecione uma opção: "))

        if opc == 1:
            print("\n" + "=" * 60)
            print("\t\tCADASTRO DE LIVROS")
            print("=" * 60)
            cadastrar_livro()
            print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

        elif opc == 2:
            print("\n" + "=" * 60)
            print("\t\tLISTAGEM DE LIVROS")
            print("=" * 60)
            lista_livros()
            print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

        elif opc == 3:
            print("\n" + "=" * 60)
            print("\t\tPESQUISA DE LIVROS")
            print("=" * 60)
            menu_pesquisa()
            print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

        elif opc == 4:
            print("\n" + "=" * 60)
            print("\t\tATUALIZAÇÃO DE LIVROS")
            print("=" * 60)
            atualizar_livro()
            print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

        elif opc == 5:
            print("\n" + "=" * 60)
            print("\t\tEXCLUSÃO DE LIVROS")
            print("=" * 60)
            excluir_livro()
            print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')

        else:
            break

    print("\n" + "=" * 60)
    print("\t\tPROGRAMA FINALIZADO")
    print("=" * 60)


def menu_pesquisa():
    while True:
        print("\n" + "-" * 40)
        print("\tMENU DE PESQUISA")
        print("-" * 40)
        print('''
    [1] - Pesquisar por ID
    [2] - Pesquisar por título
    [0] - Voltar
        ''')

        try:
            escolha = int(input("\nEscolha uma opção: "))

        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
            continue

        if escolha < 0 or escolha > 2:
            print("\nERRO: Informe um valor entre zero e dois.")

        elif escolha == 0:
            break

        elif escolha == 1:
            pesquisar_por_id()

        elif escolha == 2:
            pesquisar_por_titulo()

    print('''
    [1] - Cadastrar livro
    [2] - Listar livros
    [3] - Pesquisar livro
    [4] - Atualizar livro
    [5] - Excluir livro
    [0] - Sair
    ''')
menu()