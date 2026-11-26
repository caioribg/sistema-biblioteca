import json
from datetime import date

ano_atual = date.today().year

#1) Abertura e leitura do arquivo JSON:
def cadastrar_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)
#2) Geração automática do ID:   
    if not livros:
        identificador = 1
    else:
        maior_id = 0

        for livro in livros:
            if livro["id"] > maior_id:
                maior_id = livro["id"]
            
        identificador = maior_id + 1

#3) Entrada e validação dos dados:

    #1.0)  Validação do TÍTULO
    titulo = input("Título do livro: ").strip()
    while not titulo:
        print("\nERRO: Informe o título do livro.\nTente novamente.", end=" ")
        titulo = input("Título do livro: ").strip()

    #1.1) Validação do AUTOR
    autor = input("Nome do autor: ").strip()
    while not autor:
        print("\nERRO: Informe o nome do autor.\nTente novamente.", end=" ")
        autor = input("Nome do autor: ").strip()

    #1.2) Validação da EDITORA
    editora = input("Nome da editora: ").strip()
    while not editora:
        print("\nERRO: Informe o nome da editora.\nTente Novamente.", end=" ")
        editora = input("Nome da editora: ").strip()

    #1.3) Validação do ANO:
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano <= 0 or ano > ano_atual:
                print(f"\nERRO: Ano inválido.\nTente novamente.", end=" ")
            else:
                break

        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
   
    #1.4) Validação da QUANTIDADE:
    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            if quantidade < 0:
                print("\nERRO: Informe um valor positivo ou igual a zero.\nTente novamente.",end=" ")
            
            else:
                break
        
        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
    
    #1.5) Validação do ISBN:
    isbn = input("ISBN do livro: ").strip()
    while True:
        isbn_existente = False

        while not isbn:
            print("\nERRO: Informe o ISBN.\nTente novamente.", end=" ")
            isbn = input("ISBN do livro: ").strip()
        
        
        while not isbn.isdigit():
            print("\nERRO: O ISBN deve conter somente números.\nTente novamente.", end=" ")
            isbn = input("ISBN do livro: ").strip()
            
        for livro in livros:
            if livro["isbn"] == isbn:
                isbn_existente = True

        if isbn_existente:
            print("\nERRO: ISBNs iguais, informe o ISBN correto.\nTente novamente.",end=" ")
            isbn = input("ISBN do livro: ").strip()
        
        else:
            break      

#4) Criação do dicionário do livro        
    livro = {
        "id": identificador,
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "ano": ano,
        "isbn": isbn,
        "quantidade": quantidade
    }
 
    livros.append(livro)
    
#5) Gravando os dados no arquivo JSON:
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)

def lista_livros():
    
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    if not livros:
        print("\nBiblioteca vazia. Não há livros cadastrados.")
        return
    
    for livro in livros:
        print(f'''
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
ISBN: {livro["isbn"]}
Ano: {livro["ano"]}
Quantidade: {livro["quantidade"]}''')
        print("______________________")

def pesquisar_por_id():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

        while True:
            try:
                id_livro = int(input("Digite o ID do livro: "))

                if id_livro <= 0:
                    print("\nERRO: Informe um número positivo.\nTente novamente.", end=" ")
                    continue
                    
            except ValueError:
                print("\nERRO: Informe um valor numérico.\nTente novamente.",end=" ") 
                continue
            break

        for livro in livros:
            if livro["id"] == id_livro:
                print(f'''
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')
                break
        
        else: 
            print("\nLivro não encontrado")

def pesquisar_por_titulo():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

        livro_encontrado = False
        titulo_livro = input("Digite o título do livro: ").lower().strip()

        for livro in livros:
            if titulo_livro in livro["titulo"].lower():
                print("Livro Encontrado. ")
                livro_encontrado = True
                print(f'''
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')
        if not livro_encontrado:
            print("Livro não encontrado.")

def atualizar_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    while True:
        try:
            id_livro = int(input("Digite o ID do livro: "))

            if id_livro <= 0:
                print("\nERRO: Informe um número positivo.\nTente novamente.", end=" ")
                continue
                
        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.",end=" ") 
            continue
        break

    for livro in livros:
        if livro["id"] == id_livro:
            print(f'''
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')
            print('''1 - Alterar título
2 - Alterar autor
3 - Alterar editora
4 - Alterar ano
5 - Alterar isbn
6 - Alterar quantidade
0 - Voltar''')

            while True:
                try:
                    escolha = int(input("\nEscolha uma opção: "))
                    if escolha < 0 or escolha > 6:
                        print("\nERRO: Informe um valor entre 0 e 6.")
                        continue
                    
                    elif escolha == 1:
                        novo_titulo = input("Digite o novo título: ").strip()
                        while not novo_titulo:
                            print("ERRO: O título não pode ficar vazio.")
                            novo_titulo = input("Digite o novo título: ").strip()

                        livro["titulo"] = novo_titulo

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nTítulo atualizado com sucesso!")
                    
                    elif escolha == 2:
                        novo_autor = input("Digite o nome do novo autor: ").strip()
                        while not novo_autor:
                            print("ERRO: O autor não pode ficar vazio.")
                            novo_autor = input("Digite o nome do novo autor: ").strip()

                        livro["autor"] = novo_autor

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)
                        
                        print("\nAutor atualizado com sucesso!")

                    elif escolha == 3:
                        nova_editora = input("Digite a nova editora: ").strip()
                        while not nova_editora:
                            print("ERRO: A editora não pode ficar vazia.")
                            nova_editora = input("Digite a nova editora: ").strip()
                        
                        livro["editora"] = nova_editora

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)
                        
                        print("\nEditora atualizada com sucesso!")

                    elif escolha == 4:
                        while True:
                            try:
                                novo_ano = int(input("Ano de publicação: "))
                                if novo_ano <= 0 or novo_ano > ano_atual:
                                    print(f"\nERRO: Ano inválido.\nTente novamente.", end=" ")
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
                        
                        livro["ano"] = novo_ano

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)
                        
                        print("\nAno atualizado com sucesso!")
                    
                    elif escolha == 5:
                        novo_isbn = input("ISBN do livro: ").strip()
                        while True:
                            isbn_existente = False

                            while not novo_isbn:
                                print("\nERRO: Informe o ISBN.\nTente novamente.", end=" ")
                                novo_isbn = input("ISBN do livro: ").strip()
                            
                            
                            while not novo_isbn.isdigit():
                                print("\nERRO: O ISBN deve conter somente números.\nTente novamente.", end=" ")
                                novo_isbn = input("ISBN do livro: ").strip()
                                
                            for outro_livro in livros:
                                if outro_livro["id"] != id_livro:
                                    if outro_livro["isbn"] == novo_isbn:
                                        isbn_existente = True
                                        break
                                    
                            if isbn_existente:
                                print("\nERRO: ISBNs iguais, informe o ISBN correto.\nTente novamente.",end=" ")
                                novo_isbn = input("ISBN do livro: ").strip()
        
                            else:
                                break
                                
                        livro["isbn"] = novo_isbn
                    
                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)
                    
                        print("\nISBN atualizado com sucesso!")

                    elif escolha == 6:
                        while True:
                            try:
                                nova_quantidade = int(input("Quantidade nova: "))

                                if nova_quantidade < 0:
                                    print("\nERRO: Informe um valor positivo ou igual a zero.\nTente novamente.", end=" ")
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")

                        livro["quantidade"] = nova_quantidade

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nQuantidade atualizada com sucesso!")  

                    break
                except ValueError:
                    print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
            break
    else: 
        print("\nLivro não encontrado")
        return

    


