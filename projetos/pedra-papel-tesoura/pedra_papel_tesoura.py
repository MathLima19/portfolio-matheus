# Crie um pg de um jogo de pedra papel e tesoura, que receberá duas variáveis, e o pg vai dizer quem ganhou.

print("=== Pedra, Papel ou Tesoura ===")

jogador1 = input("Jogador 1, escolha (pedra, papel ou tesoura): ").lower()  # .lower () transforma todo o texto em letras minusculas, evitando erro.
jogador2 = input("Jogador 2, escolha (pedra, papel ou tesoura): ").lower()

print("\nJogador 1 escolheu: {}".format(jogador1)) # \n coloca o print p baixo, pula a linha.
print("Jogador 2 escolheu: {}".format(jogador2))

if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") \
     or (jogador1 == "tesoura" and jogador2 == "papel") \
     or (jogador1 == "papel" and jogador2 == "pedra"):
    print("Jogador 1 venceu!") # Na linha de cima foi usado a contra barra, que quebra o cdg, jogando p linha de baixo.
elif (jogador2 == "pedra" and jogador1 == "tesoura") \
     or (jogador2 == "tesoura" and jogador1 == "papel") \
     or (jogador2 == "papel" and jogador1 == "pedra"):
    print("Jogador 2 venceu!")
else:
    print("Jogada inválida! Digite apenas pedra, papel ou tesoura.")