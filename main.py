from biblioteca import cadastrar_livro, lista_livros, pesquisar_por_id, pesquisar_por_titulo, atualizar_livro
def menu():
    print("\n")
    print(28*"-=")
    print("\tSISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print(28*"-=")

    print('''\n1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Atualizar livro
5 - Excluir livro
0 - Sair\n''')
    
    while True:

        opc = int(input("\nSelecione uma opção: "))
        while opc < 0 or opc > 5:
            print("\nERRO: Informe uma opção entre 0 e 5.\nTente novamente.", end="\n")
            
            opc = int(input("Selecione uma opção: "))

        if opc == 1:
            print(28*"-=")
            print("\t\tCADASTRAR LIVRO")
            print(28*"-=")
            cadastrar_livro()
            print('''\n1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Atualizar livro
5 - Excluir livro
0 - Sair\n''')
            
        
        elif opc == 2:
            print(28*"-=")
            print("\t\tLISTAR LIVROS")
            print(28*"-=")
            lista_livros()
            print('''\n1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Atualizar livro
5 - Excluir livro
0 - Sair\n''')
        
        elif opc == 3:
            print(28*"-=")
            print("\t\tPESQUISAR LIVROS")
            print(28*"-=")
            menu_pesquisa()
        
        elif opc == 4:
            print(28*"-=")
            print("\t\tATUALIZAR LIVRO")
            print(28*"-=")
            atualizar_livro()
            print('''\n1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Atualizar livro
5 - Excluir livro
0 - Sair\n''')

        elif opc == 5:
            print(28*"-=")
            print("\t\tEXCLUIR LIVRO")
            print(28*"-=")
        
        else:
            break
        
    print(28*"-=")
    print("\tPROGRAMA FINALIZADO")
    print(28*"-=")


def menu_pesquisa():
    while True:
        print("1 - Pesquisar por ID")
        print("2 - Pesquisar por Título")
        print("0 - Voltar")
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
            
    print('''\n1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Atualizar livro
5 - Excluir livro
0 - Sair\n''')
menu()

