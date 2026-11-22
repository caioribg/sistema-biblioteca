from biblioteca import cadastrar_livro
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

        opc = int(input("\nEscolha uma opção: "))
        while opc < 0 or opc > 5:
            print("\nERRO: Informe uma opção entre 0 e 5.\nTente novamente.", end=" ")
            opc = int(input("Escolha uma opção: "))

        if opc == 1:
            print(28*"-=")
            print("\t\tCADASTRAR LIVRO")
            print(28*"-=")
            cadastrar_livro()
            
        
        elif opc == 2:
            print(28*"-=")
            print("\t\tLISTAR LIVROS")
            print(28*"-=")
        
        elif opc == 3:
            print(28*"-=")
            print("\t\tPESQUISAR LIVROS")
            print(28*"-=")
        
        elif opc == 4:
            print(28*"-=")
            print("\t\tATUALIZAR LIVRO")
            print(28*"-=")

        elif opc == 5:
            print(28*"-=")
            print("\t\tEXCLUIR LIVRO")
            print(28*"-=")
        
        else:
            break
        
    print(28*"-=")
    print("\tPROGRAMA FINALIZADO")
    print(28*"-=")
menu()

