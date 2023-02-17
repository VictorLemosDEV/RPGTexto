from colors import *
import time

# Arquivo para armazenar funções genéricas como diálogos e perguntas.


def EscreverTypeWriter(text: str, intervalInSeconds: int = 0.05):
  for x in text:
    print(x,end="",flush=True)
    time.sleep(intervalInSeconds)
  print(f"{ResetColor}")
  

# def PerguntaBooleana(pergunta: Pergunta em formato string)
#Gera uma pergunta que o usuário só pode responder com sim ou não.
def PerguntaBooleana(pergunta: str) -> True or False:
  respostaPergunta = input(pergunta + " s/n \n")

  if respostaPergunta.lower() in ["sim", "s"]:
    return True
  elif respostaPergunta.lower() in ["não", "nao", "n"]:
    return False
  else:
    #print(f"{main.BrightRed}Você só pode responder essa pergunta com sim ou não!")
    PerguntaBooleana(pergunta)


#def ChecarInventario(categoria: Categoria em formato string(opcional))
'''
def ChecarInventario(categoria: str = None):

  if categoria == None:
  

    print(f"Carregando inventário do Fracassado...")
    time.sleep(0.5)

    print(f"{main.BrightWhite}---------Dados Genéricos do Fracassado-----------------{main.Reset}")
    time.sleep(0.1)
    print(f"NOME DO FRACASSADO: {main.PerfilDoFracassado['Nome']}")
    time.sleep(0.1)
    print(f"IDADE DO FRACASSADO: {main.PerfilDoFracassado['Idade']}")
    time.sleep(0.1)
    print(f"IDADE DO FRACASSADO: {main.PerfilDoFracassado['Idade']}")
  else:
    print(f"Carrendo informação do Fracassado...")
    time.sleep(0.3)
    if main.PerfilDoFracassado[categoria]:
      print(f"{categoria} do FRACASSADO: {main.PerfilDoFracassado[categoria]}")
    else:
      print("O FRACASSADO NÃO SABE NEM QUAIS SÃO SUAS CATEGORIAS DO INVENTARIO!")

'''
