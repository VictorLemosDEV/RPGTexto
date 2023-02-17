# Cuida de todas as informações do jogo e do jogador

import json

defaultData = {"hasPlayedBefore": False}



def SaveData(dataToSave=defaultData, saveFile="saves.json"):

  
  with open(saveFile, mode="w") as File:

    File.writelines(json.dumps(dataToSave))



def LoadData(saveFile="saves.json"):
  with open(saveFile, "r") as File:

      data = json.loads(File.read())
      return data
