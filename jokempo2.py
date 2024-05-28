import random

def jokenpo():
    choices = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(choices)
    user_choice = input("Escolha pedra, papel ou tesoura: ").lower()

    print(f"Computador escolheu: {computer_choice}")

    if user_choice == computer_choice:
        print("Empate!")
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
         (user_choice == "tesoura" and computer_choice == "papel") or \
         (user_choice == "papel" and computer_choice == "pedra"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

jokenpo()