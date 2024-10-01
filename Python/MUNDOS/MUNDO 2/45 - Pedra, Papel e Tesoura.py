from random import choice
jokenpo = ["Pedra", "Papel", "Tesoura"]
x = choice(jokenpo)

escolha = str(input("Pedra, Papel ou Tesoura? Digite sua escolha: "))
escolha = escolha.lower().strip()

if x == "Pedra" and escolha == "pedra":
    print("Eu escolhi {}, e você escolheu {}. Deu empate, vamos tentar de novo!".format(x, escolha))
elif x == "Pedra" and escolha == "papel":
    print("Eu escolhi {} e você escolheu {}. Você venceu, eu perdi! Você deu sorte dessa vez".format(x, escolha))
elif x == "Pedra" and escolha == "tesoura":
    print("Eu escolhi {} e você escolheu {}. Eu ganhei, tente novamente!".format(x, escolha))
elif x == "Papel" and escolha == "pedra":
    print("Eu escolhi {} e você escolheu {}. Eu ganhei, tente novamente!".format(x, escolha))
elif x == "Papel" and escolha == "papel":
    print("Eu escolhi {}, e você escolheu {}. Deu empate, vamos tentar de novo!".format(x, escolha))
elif x == "Papel" and escolha == "tesoura":
    print("Eu escolhi {} e você escolheu {}. Você venceu, eu perdi! Você deu sorte dessa vez".format(x, escolha))
elif x == "Tesoura" and escolha == "pedra":
    print("Eu escolhi {} e você escolheu {}. Você venceu, eu perdi! Você deu sorte dessa vez".format(x, escolha))
elif x == "Tesoura" and escolha == "papel":
    print("Eu escolhi {} e você escolheu {}. Eu ganhei, tente novamente!".format(x, escolha))
elif x == "Tesoura" and escolha == "tesoura":
    print("Eu escolhi {}, e você escolheu {}. Deu empate, vamos tentar de novo!".format(x, escolha))

