import forca
import adivinhacao

print("*********************************")
print("*********Escolha um jogo*********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if (jogo == 1):
    print("Jogando Forca") 
elif (jogo == 2):
    print("Jogando Adivinhação")