#. ATENÇÃO! ● PEDRA GANHA DA TESOURA; ● PAPEL GANHA DA PEDRA; ● TESOURA GANHA DO PAPEL

jogador1 = input("Jogador 1: digite seu nome  ")
jogador2 = input("Jogador 2: digite seu nome  ")

escolha1 = input(f" {jogador1} escolha sua opção: Pedra | Papel | Tesoura: ")
escolha2 = input(f" {jogador2} escolha sua opção: Pedra | Papel | Tesoura: ")

if escolha1 == "Pedra" or "pedra" and escolha2 == "Tesoura" or "tesoura":
    print(f'O jogador {jogador1} venceu!')

elif escolha2 == "Pedra" or "pedra" and escolha1 == "Tesoura" or "tesoura":
    print(f'O jogador {jogador2} venceu!')

elif escolha1 == "Pepel" or "papel" and escolha2 ==  "Pedra" or "pedra":
    print(f'O jogador {jogador1} venceu!')

elif escolha2 == "Pepel" or "papel" and escolha1 ==  "Pedra" or "pedra":
    print(f'O jogador {jogador2} venceu!')

elif escolha1 == "Tesoura" or "tesoura" and escolha2 == "Pepel" or "papel":
    print(f'O jogador {jogador1} venceu!')

elif escolha2 == "Tesoura" or "tesoura" and escolha1 == "Pepel" or "papel":
    print(f'O jogador {jogador2} venceu!')

else:
    print(f'Houve um EMPATE entre os jogadores {jogador1} e {jogador2}!')
