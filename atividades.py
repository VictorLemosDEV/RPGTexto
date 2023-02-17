def verifica_aluno_aprovado():
  try:
    nota = float(input("Digite sua nota seu fracassado: "))
  
    frequencia = int(input("Digite sua frequencia em %: "))

    if nota >= 7 and frequencia >= 70:
      print("Aprovado!")
    else:
      print("Reprovado.")
    return
  except ValueError:
    print("Você é um animal!")

verifica_aluno_aprovado()
