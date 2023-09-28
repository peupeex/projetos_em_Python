salto = int(input("digite o salto de letras, MÁXIMO DE 26: "))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
alfabetom = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

texto = input("digite o texto: ")

secret = ''

for palavra in texto:
    if palavra in alfabeto:
        posicao = alfabeto.find(palavra)
        posicao += salto
        if posicao >= len(alfabeto):
            posicao = posicao % len(alfabeto)
        secret += alfabeto[posicao]

    elif palavra in alfabetom:
        posicao = alfabetom.find(palavra)
        posicao += salto
        if posicao >= len(alfabetom):
            posicao = posicao % len(alfabetom)
        secret += alfabetom[posicao]
    
    else:
        secret += palavra

print("mensagem criptografada: " + secret)

