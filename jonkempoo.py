import random

rodadas = int(input("Quantas rodadas?  "))
vitorias_humano = 0
vitorias_pc = 0

while (rodadas > 0):

  def escolha1():
    print("Escolha uma das opções abaixo")
    print("1 - pedra")
    print("2 - papel")
    print("3 - tesoura")
    humano = int(input(":  "))
    return humano

  def escolha2():
    opcoes = [1, 2, 3]
    computador = random.choice(opcoes)
    return computador

  eu = escolha1()
  pc = escolha2()


  def compare(jog1, jog2):
    global vitorias_humano
    global vitorias_pc

    if (jog1 == jog2):
      print("!!!Empate!!!")

    elif (jog1 == 1 and jog2 == 2):
      print("O computador ganhou esta rodada...")
      vitorias_pc += 1

    elif (jog1 == 1 and jog2 == 3):
      print("O humano ganhou esta rodada...")
      vitorias_humano += 1

    elif (jog1 == 2 and jog2 == 1):
      print("O humano ganhou esta rodada...")
      vitorias_humano += 1

    elif (jog1 == 2 and jog2 == 3):
      print("O computador ganhou esta rodada...")
      vitorias_pc += 1

    elif (jog1 == 3 and jog2 == 1):
      print("O computador ganhou esta rodada...")
      vitorias_pc += 1

    elif (jog1 == 3 and jog2 == 2):
      print("O humano ganhou esta rodada...")
      vitorias_humano += 1


  def conversao1(jog):
    if (jog == 1):
      print("Humano: PEDRA")
    elif (jog == 2):
      print("Humano: PAPEL")
    elif (jog == 3):
      print("Humano: TESOURA")
    else:
      print("Você escoleu uma opção inválida")

  def conversao2(jog):
    if (jog == 1):
      print("Computador: PEDRA")
    if (jog == 2):
      print("Computador: PAPEL")
    else:
      print("Computador: TESOURA")

  rodadas -= 1

  conversao1(eu)
  conversao2(pc)
  compare(eu, pc)


print("Numero total de vitórias do humano:" , vitorias_humano)
print("Numero total de vitrias do computador: ", vitorias_pc)

  