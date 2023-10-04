#. ATENÇÃO! PEDRA GANHA DA TESOURA; ● PAPEL GANHA DA PEDRA; ● TESOURA GANHA DO PAPEL

jogador1 = input("Jogador 1, digite seu nome: ")
jogador2 = input("Jogador 2, digite seu nome: ")

resp = "S"
while resp == "S" or resp == "s":
    escolha1 = int(input(f" {jogador1} escolha sua opção: 1° Pedra | 2° Papel | 3° Tesoura: "))
    escolha2 = int(input(f" {jogador2} escolha sua opção: 1° Pedra | 2° Papel | 3° Tesoura: "))

    if escolha1 == 1 and escolha2 == 3:
        print(f'O jogador {jogador1} venceu!')

    elif escolha2 == 1 and escolha1 == 3:
        print(f'O jogador {jogador2} venceu!')

    elif escolha1 == 2 and escolha2 == 1:
        print(f'O jogador {jogador1} venceu!')

    elif escolha2 == 2 and escolha1 == 1:
        print(f'O jogador {jogador2} venceu!')

    elif escolha1 == 3 and escolha2 == 2:
        print(f'O jogador {jogador1} venceu!')

    elif escolha2 == 3 and escolha1 == 2:
        print(f'O jogador {jogador2} venceu!')

    else:
        print(f'Houve um EMPATE entre os jogadores {jogador1} e {jogador2}!')
        resp = input("Deseja jogar novamente S = sim | N = não? ")
        if resp == "N":
            break

print("Fim de jogo!")