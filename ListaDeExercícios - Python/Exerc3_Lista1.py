#Função para imprimir tabuleiro de xadrez(8x8)

def tabuleiroXadrez():

    linha = 8
    coluna  = 8

    for i in range(linha):
        for j in range(coluna):
            if(linha+coluna)%2 == 0:
                print("{: ^10} {:*^10}".format("",""),end="")
            else:
                 print("{:*^10}{:^10}".format("","") ,end="")
        print()
    print()
    return True

print(tabuleiroXadrez())




