import random

def jogar_jokenpo():
  opcoes = ['pedra', 'papel', 'tesoura']

  jogador1_vitorias = 0
  jogador2_vitorias = 0

  num_partidas = int(input("Quantas partidas você deseja jogar? "))

  for _ in range(num_partidas):
    print("Jogador 1, escolha pedra, papel ou tesoura: ")
    jogador1_escolha = input("jogador 1: ").lower()
    jogador2_escolha = random.choice(opcoes)

    print("Jogador 2 escolheu:", jogador2_escolha)

    if jogador1_escolha in opcoes:
      if jogador1_escolha == jogador2_escolha:
        print("Empate!")
      elif (jogador1_escolha == 'pedra' and jogador2_escolha == 'tesoura') or \
        (jogador1_escolha == 'papel' and jogador2_escolha == 'pedra') or \
        (jogador1_escolha == 'tesoura' and jogador2_escolha == 'papel'):
        print("Jogador 1 venceu!")
        jogador1_vitorias += 1
      else:
        print("Jogador 2 venceu!")
        jogador2_vitorias += 1
    else:
      print("Escolha inválida!")

  print("\nResultado final:")
  print("Jogador 1:", jogador1_vitorias, "vitórias")
  print("Jogador 2:", jogador2_vitorias, "vitórias")

jogar_jokenpo()