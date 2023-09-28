nome_de_usuario = []
idade_de_usuario = []

def busca(pesq):
    for indice, nome in enumerate(nome_de_usuario):
        if nome == pesq:
            print("Nome:", nome)
            print("Idade:", idade_de_usuario[indice])
            return indice + 1
    return -1

def remover(pesq):
    indice = busca(pesq)
    if indice != -1:
        nome_de_usuario.pop(indice - 1)
        idade_de_usuario.pop(indice - 1)
        return "Usuário removido com sucesso."
    else:
        return "Usuário não encontrado."

while True:
    print("1. Registrar um novo usuário.")
    print("2. Listar todos os usuários.")
    print("3. Buscar usuário por nnome.")
    print("4. Apagar usuário.")
    print("5. Sair do cadastro.")

    try:
        escolha_numero = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Por favor, escolha um número de 1 a 4.")
        continue

    if escolha_numero == 1:
        nome = input("Informe o nome de usuário: ")
        idade = int(input("Informe a idade do usuário: "))
        nome_de_usuario.append(nome)
        idade_de_usuario.append(idade)
    elif escolha_numero == 2:
        for indice, nome in enumerate(nome_de_usuario):
            print(f"Nome: {nome} Idade: {idade_de_usuario[indice]}")
    elif escolha_numero == 3:
        nome_pesquisa = input("Informe o nome do usuário a ser pesquisado: ")
        resultado_busca = busca(nome_pesquisa)
        if resultado_busca != -1:
            print(f"Usuário encontrado na posição {resultado_busca}.")
        else:
            print("Usuário não encontrado.")
    elif escolha_numero == 4:
        nome_remover = input("Digite o usuário a ser removido: ")
        resultado_remover = remover(nome_remover)
        print(resultado_remover)
    elif escolha_numero == 5:
        break
