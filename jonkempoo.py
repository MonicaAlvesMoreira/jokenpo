import random

def escolha_palavra():
    palavra_pc = [1, 2, 3]
    return random.choice(palavra_pc)

def conversao(eu, pc):
    if (eu == 1):
        print("Humano: PEDRA")
    elif (eu == 2):
        print("Humano: PAPEL")
    else:
        print("Humano: TESOURA")

    if (pc == 1):
        print("Computador: PEDRA")
    elif (pc == 2):
        print("Computador: PAPEL")
    else:
        print("Computador: TESOURA")

    

print("escolha uma das opções: ")
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")
palavra_eu = int(input(": "))
palavra_pc = escolha_palavra()


def comparacao (eu, pc):
    if (eu == pc):
        print("EMPATE!!!")
    elif (eu == 1 and pc == 2):
        print("O computador ganhou")
    elif (eu == 1 and pc == 3):
        print("O Humano ganhou")
    elif (eu == 2 and pc == 1):
        print("O Humano ganhou!")
    elif (eu == 2 and pc == 3):
        print("O computador ganhou")
    elif (eu == 3  and pc == 1):
        print("O computador ganhou")
    elif (eu == 3 and pc == 2):
        print("Humano ganhou")
    else:
        print("Vc digitou errado...")


escolha_palavra()
print
print(palavra_pc)
print(palavra_eu)

conversao(palavra_eu, palavra_pc)
comparacao(palavra_eu, palavra_pc)