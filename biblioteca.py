
import json
from datetime import date

ano_atual = date.today().year


# ============================================================
# CADASTRAR LIVRO
# ============================================================

def cadastrar_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    # Geração automática do ID
    if not livros:
        identificador = 1
    else:
        maior_id = 0

        for livro in livros:
            if livro["id"] > maior_id:
                maior_id = livro["id"]

        identificador = maior_id + 1

    # Entrada e validação dos dados

    # Título
    print("\n" + "-" * 50)
    print("\tCADASTRO DE LIVRO")
    print("-" * 50)

    titulo = input("Título do livro: ").strip()
    while not titulo:
        print("\nERRO: Informe o título do livro.")
        titulo = input("Título do livro: ").strip()

    # Autor
    autor = input("Nome do autor: ").strip()
    while not autor:
        print("\nERRO: Informe o nome do autor.")
        autor = input("Nome do autor: ").strip()

    # Editora
    editora = input("Nome da editora: ").strip()
    while not editora:
        print("\nERRO: Informe o nome da editora.")
        editora = input("Nome da editora: ").strip()

    # Ano
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano <= 0 or ano > ano_atual:
                print("\nERRO: Ano inválido. Tente novamente.")
            else:
                break

        except ValueError:
            print("\nERRO: Informe um valor numérico.")

    # Quantidade
    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            if quantidade < 0:
                print("\nERRO: Informe um valor positivo ou igual a zero.")
            else:
                break

        except ValueError:
            print("\nERRO: Informe um valor numérico.")

    # ISBN
    isbn = input("ISBN do livro: ").strip()
    while True:
        isbn_existente = False

        while not isbn:
            print("\nERRO: Informe o ISBN.")
            isbn = input("ISBN do livro: ").strip()

        while not isbn.isdigit():
            print("\nERRO: O ISBN deve conter somente números.")
            isbn = input("ISBN do livro: ").strip()

        for livro in livros:
            if livro["isbn"] == isbn:
                isbn_existente = True

        if isbn_existente:
            print("\nERRO: ISBN já cadastrado. Informe outro ISBN.")
            isbn = input("ISBN do livro: ").strip()
        else:
            break

    # Criação do dicionário
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

    # Gravação no JSON
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)

    print("\n" + "=" * 50)
    print("\tLIVRO CADASTRADO COM SUCESSO!")
    print("=" * 50)


# ============================================================
# LISTAR LIVROS
# ============================================================

def lista_livros():

    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    if not livros:
        print("\n" + "-" * 50)
        print("\tBIBLIOTECA VAZIA")
        print("-" * 50)
        print("Não há livros cadastrados.")
        return

    print("\n" + "=" * 50)
    print("\tLIVROS CADASTRADOS")
    print("=" * 50)

    for livro in livros:
        print(f'''
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
ISBN: {livro["isbn"]}
Ano: {livro["ano"]}
Quantidade: {livro["quantidade"]}
''')
        print("-" * 50)


# ============================================================
# PESQUISAR LIVRO POR ID
# ============================================================

def pesquisar_por_id():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

        while True:
            try:
                id_livro = int(input("Digite o ID do livro: "))

                if id_livro <= 0:
                    print("\nERRO: Informe um número positivo.")
                    continue

            except ValueError:
                print("\nERRO: Informe um valor numérico.")
                continue

            break

        for livro in livros:
            if livro["id"] == id_livro:
                print("\n" + "=" * 50)
                print("\tLIVRO ENCONTRADO")
                print("=" * 50)

                print(f'''
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')
                break

        else:
            print("\nLIVRO NÃO ENCONTRADO.")


# ============================================================
# PESQUISAR LIVRO POR TÍTULO
# ============================================================

def pesquisar_por_titulo():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

        livro_encontrado = False

        while True:
            titulo_livro = input("Digite o título do livro: ").lower().strip()

            if not titulo_livro:
                print("\nERRO: Informe um título para pesquisar.")
                continue
            
            break

        for livro in livros:
            if titulo_livro in livro["titulo"].lower():
                print("\n" + "=" * 50)
                print("\tLIVRO ENCONTRADO")
                print("=" * 50)

                livro_encontrado = True

                print(f'''
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')

        if not livro_encontrado:
            print("\nLIVRO NÃO ENCONTRADO.")


# ============================================================
# ATUALIZAR LIVRO
# ============================================================

def atualizar_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    while True:
        try:
            id_livro = int(input("Digite o ID do livro: "))

            if id_livro <= 0:
                print("\nERRO: Informe um número positivo.")
                continue

        except ValueError:
            print("\nERRO: Informe um valor numérico.")
            continue

        break

    for livro in livros:
        if livro["id"] == id_livro:
            print("\n" + "=" * 50)
            print("\tDADOS DO LIVRO")
            print("=" * 50)

            print(f'''
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')

            print("-" * 50)
            print("\tMENU DE ATUALIZAÇÃO")
            print("-" * 50)

            print('''1 - Alterar título
2 - Alterar autor
3 - Alterar editora
4 - Alterar ano
5 - Alterar ISBN
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
                            print("\nERRO: O título não pode ficar vazio.")
                            novo_titulo = input("Digite o novo título: ").strip()

                        livro["titulo"] = novo_titulo

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nTítulo atualizado com sucesso!")

                    elif escolha == 2:
                        novo_autor = input("Digite o nome do novo autor: ").strip()
                        while not novo_autor:
                            print("\nERRO: O autor não pode ficar vazio.")
                            novo_autor = input("Digite o nome do novo autor: ").strip()

                        livro["autor"] = novo_autor

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nAutor atualizado com sucesso!")

                    elif escolha == 3:
                        nova_editora = input("Digite a nova editora: ").strip()
                        while not nova_editora:
                            print("\nERRO: A editora não pode ficar vazia.")
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
                                    print("\nERRO: Ano inválido. Tente novamente.")
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("\nERRO: Informe um valor numérico.")

                        livro["ano"] = novo_ano

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nAno atualizado com sucesso!")

                    elif escolha == 5:
                        novo_isbn = input("ISBN do livro: ").strip()
                        while True:
                            isbn_existente = False

                            while not novo_isbn:
                                print("\nERRO: Informe o ISBN.")
                                novo_isbn = input("ISBN do livro: ").strip()

                            while not novo_isbn.isdigit():
                                print("\nERRO: O ISBN deve conter somente números.")
                                novo_isbn = input("ISBN do livro: ").strip()

                            for outro_livro in livros:
                                if outro_livro["id"] != id_livro:
                                    if outro_livro["isbn"] == novo_isbn:
                                        isbn_existente = True
                                        break

                            if isbn_existente:
                                print("\nERRO: ISBN já cadastrado. Informe outro ISBN.")
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
                                    print("\nERRO: Informe um valor positivo ou igual a zero.")
                                    continue
                                else:
                                    break

                            except ValueError:
                                print("\nERRO: Informe um valor numérico.")

                        livro["quantidade"] = nova_quantidade

                        with open("dados.json", "w", encoding="utf-8") as arquivo:
                            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                        print("\nQuantidade atualizada com sucesso!")

                    break

                except ValueError:
                    print("\nERRO: Informe um valor numérico.")

            break

    else:
        print("\nLIVRO NÃO ENCONTRADO.")
        return


# ============================================================
# EXCLUIR LIVRO
# ============================================================

def excluir_livro():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        livros = json.load(arquivo)

    while True:
        try:
            id_livro = int(input("Digite o ID do livro: "))

            if id_livro <= 0:
                print("\nERRO: Informe um número positivo.")
                continue

            else:
                break

        except ValueError:
            print("\nERRO: Informe somente números.")

    for livro in livros:
        if livro["id"] == id_livro:
            print("\n" + "=" * 50)
            print("\tDADOS DO LIVRO")
            print("=" * 50)

            print(f'''
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Editora: {livro["editora"]}
Ano: {livro["ano"]}
ISBN: {livro["isbn"]}
Quantidade: {livro["quantidade"]}
''')

            while True:
                confirmação = input(
                    "Deseja realmente excluir esse livro? (S/N): "
                ).strip().upper()

                if confirmação == "S" or confirmação == "N":
                    break
                else:
                    print("\nERRO: Resposta inválida. Digite S ou N.")

            if confirmação == "S":
                livros.remove(livro)

                with open("dados.json", "w", encoding="utf-8") as arquivo:
                    json.dump(livros, arquivo, ensure_ascii=False, indent=4)

                print("\nLivro excluído com sucesso!")

            elif confirmação == "N":
                print("\nExclusão cancelada.")

            break

    else:
        print("\nLIVRO NÃO ENCONTRADO.")
