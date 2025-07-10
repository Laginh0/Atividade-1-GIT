import random

def jogo_adivinhacao(num):
  palpite = 0
  while palpite != num:
    try:
      palpite = int(input("Adivinhe o número: "))
      if palpite > num:
        print("Maior que o número secreto")
      elif palpite < num:
        print("Menor que o número secreto")
    except ValueError:
      print("Por favor, digite um número válido.")
 
  print(f"Parabéns! Você acertou o número secreto: {num}")


num_rand = random.randint(1, 100)
jogo_adivinhacao(num_rand)