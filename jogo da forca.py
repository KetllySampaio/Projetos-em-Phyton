print("Seja bem vindo(a) ao Jogo Da Forca!!")

palavra = "harry" #palavra para ser adivinhada
letras_usuario = [] #letras que o usuario ja chutou
chances = 4  #quantidade de chances
ganhou  = False



while True: #loop verdadeiro
#criar logica
    for letra in palavra:
        if letra in letras_usuario:
            print(letra,end=" ")
        else:
            print("-",end=" ")
    print(f"Você tem {chances} chances")
    tentativa=input("Escolha uma letra para adivinhar a palavra: ")
    letras_usuario.append(tentativa)

    if tentativa not in palavra:
        chances -= 1 
    
    ganhou = True
    for letra in palavra:
        if letra not in letras_usuario:
            ganhou=False

    
    if chances == 0 or ganhou:
        break


if ganhou:
    print(f"Parabéns, você ganhou! A palavra era {palavra}")

else:
    print(f"Você perdeu! A palavra era {palavra}")