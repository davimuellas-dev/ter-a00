palavra_secreta = "bool"
letras_acertadas = []
letras_erradas = []
tentativas = 30
palavra_formada = ""
while tentativas > 0:
    if palavra_formada == palavra_secreta:
        break
     
    print("Palavra formada: ", palavra_formada or "_" * len(palavra_secreta))
    print("Letras erradas: ", letras_erradas)
    print("Tentativas restantes: ", tentativas)
    letra_digitada = input("Digite uma letra: ")

    if letra_digitada in palavra_secreta:
        letras_acertadas.append(letra_digitada)
    else:
        letras_erradas.append(letra_digitada)
        tentativas -= 1

    palavra_formada = "".join(
        letra if letra in letras_acertadas else "_"
        for letra in palavra_secreta
    )

if palavra_formada == palavra_secreta:
    print("Parabéns! Você acertou a palavra!")
else:
    print("Você perdeu! A palavra era: ", palavra_secreta)