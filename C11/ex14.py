# 3. Mini Campo Minado
tabuleiro = np.zeros((2, 2), dtype=int)
linha, coluna = np.random.randint(0, 2), np.random.randint(0, 2)
tabuleiro[linha, coluna] = 1

tentativas = 0
achou = False

while tentativas < 3 and not achou:
    x = int(input("Digite a linha (0 ou 1): "))
    y = int(input("Digite a coluna (0 ou 1): "))

    if tabuleiro[x, y] == 1:
        print("Game Over! :( Try Again!")
        achou = True
    else:
        print("Seguro! Continue jogando.")
    tentativas += 1

if not achou:
    print("Congratulations! You beat the game! :)")
