import forca
import adivinhacao
import os

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Adivinhação")
print("(2) Forca")

jogo = int(input("Qual jogo? "))

while (jogo not in range(1,3)):
    os.system("cls")
    print("Jogo inválido! Digite 1 ou 2")
    jogo = int(input("Qual jogo? "))

os.system("cls")

if (jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
else:
    print("Jogando Forca")
    forca.jogar()

