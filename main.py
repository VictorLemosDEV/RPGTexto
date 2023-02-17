#Importando Módulos
import random
import time

from functions import *
import saves
from colors import *

# Variáveis de Inicialização
GameStart = False
dataLoaded = False
data = None



while dataLoaded != True:
  try:
    data = saves.LoadData()
    dataLoaded = True
  except FileNotFoundError:  # Caso o arquivo ainda não esteja criado
    saves.SaveData()

if not dataLoaded:
  raise (ValueError)


if data["hasPlayedBefore"] == False:
  nomeDoFracassado = input("Digite seu nome seu fracassado: ")
  print("Que nome bosta")
  idadeDoFracassado = int(input('Digite sua idade fracassado: '))

  if idadeDoFracassado <= 18:
    print("Parece uma garota de anime com 84858347583758 anos!")

  generoDoFracassado = input("Digite seu gênero seu fracassado!: ")

  if generoDoFracassado == "MACHO":
    print("Pra poder lutar tem que ser MACHO de verdade!")
  else:
    print("Isso aí é marca de sabão em pó?")

  PerfilDoFracassado = {}
  PerfilDoFracassado["Nome"] = nomeDoFracassado
  PerfilDoFracassado["Idade"] = idadeDoFracassado
  PerfilDoFracassado["Genero"] = generoDoFracassado
  PerfilDoFracassado["Moedas"] = 0  #A gente é pobre

  PerfilDoFracassado["hasPlayedBefore"] = True
  saves.SaveData(PerfilDoFracassado)

iniciar = input(f"Aperte Enter para iniciar o jogo!")

PerfilDoFracassado = data

GameStart = True

time.sleep(3)

if GameStart == True:
  #Aqui dentro a gente faz o resto do jogo
  EscreverTypeWriter(f"\nAgora você é oficialmente um {BrightRed}FRACASSADO{ResetColor} NA VIDA!",0.05)
  time.sleep(3)
  EscreverTypeWriter(f"Um homem bem vestido se aproxima e lhe dá...", 0.05)
  time.sleep(1)
  #Primeiro valor é o mínimo e o segundo é o maximo
  moedasParaReceber = random.randint(2, 20)
  PerfilDoFracassado["Moedas"] += moedasParaReceber

  print(f"{BrightBlue}{moedasParaReceber} moedas! {ResetColor}")
  

time.sleep(1.5)
agradecer = PerguntaBooleana("Você agradece?")

if agradecer:

  EscreverTypeWriter(f"{Blue}Não foi nada! Boa sorte em sua viagem...",0.05)

else:
  EscreverTypeWriter(f"{Red}Mau agradecido!",0.05)
