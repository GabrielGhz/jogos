def jogar():
    print("*********************************")
    print("****Bem vindo ao jogo Forca!*****")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    print(palavras)

    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]  


    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() #cortar as barras invisivéis que o usuário escreveu e deixar maiúsculas

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você Perdeu!!")
    print("Fim de jogo")

if(__name__=="__main__"):
    jogar()
