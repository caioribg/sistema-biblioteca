import json
from datetime import date

ano_atual = date.today().year


def cadastrar_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)
    
    if not livros:
        identificador = 1
    else:
        maior_id = 0

        for livro in livros:
            if livro["id"] > maior_id:
                maior_id = livro["id"]
            
        identificador = maior_id + 1
    
    titulo = input("Título do livro: ").strip()
    while not titulo:
        print("\nERRO: Informe o título do livro.\nTente novamente.", end=" ")
        titulo = input("Título do livro: ").strip()

    autor = input("Nome do autor: ").strip()
    while not autor:
        print("\nERRO: Informe o nome do autor.\nTente novamente.", end=" ")
        autor = input("Nome do autor: ").strip()

    editora = input("Nome da editora: ").strip()
    while not editora:
        print("\nERRO: Informe o nome da editora.\nTente Novamente.", end=" ")
        editora = input("Nome da editora: ").strip()

    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano <= 0 or ano > ano_atual:
                print(f"\nERRO: Ano inválido.\nTente novamente.", end=" ")
            else:
                break

        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
    
    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            if quantidade < 0:
                print("\nERRO: Informe um valor positivo ou igual a zero.\nTente novamente.",end=" ")
            
            else:
                break
        
        except ValueError:
            print("\nERRO: Informe um valor numérico.\nTente novamente.", end=" ")
    
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

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)
