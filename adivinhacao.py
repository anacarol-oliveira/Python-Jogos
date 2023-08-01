import random
import os

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    nivel = int(input("Escolha o nível: "))

    while (nivel not in range (1,4)):
        os.system("cls")
        print("Valor inválido! Digite 1, 2 ou 3")
        nivel = int(input("Escolha o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5

    os.system("cls")

    for rodada in range(1, tentativas + 1):

        print("Rodada {} de {} tentativas".format(rodada, tentativas))
        chute = int(input("Chute um número entre 1 e 100: "))
        os.system("cls")

        if(chute not in range(1,101)):
            print("Número inválido!")
            continue

        os.system("cls")

        if (chute == numero_secreto):
            print("Você digitou {}".format(chute))
            print("Você acertou! Pontuação: {}/1000".format(pontos))
            break
        else:
            if (chute > numero_secreto):
                print("Você digitou {}".format(chute))
                print("Você errou! O seu chute foi maior do que o número secreto.")
            else:
                print("Você digitou {}".format(chute))
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(rodada == tentativas):
                print("As tentativas acabaram! O número secreto era {}".format(numero_secreto))

    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()