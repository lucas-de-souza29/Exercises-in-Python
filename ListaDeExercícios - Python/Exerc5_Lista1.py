
#Função recebe número e retorna noves-fora

def novesFora():
    resultado = 0
    divisor = 2
    quociente = 0

    #Teste será sobre o exemplo dado na lista número 131
    nro = int(input("Informe um numero : "))
    quociente = (int(nro/2))

    #quociente será 65 com resto 1 mediante aos cálculos feitos na mão

    resto = 1
    print("Quociente e resto", quociente, resto)

    decomposicaoNroDividendo = 1+3+1

    somaDoQuocienteDesmembrado = 6+5
    resultado = somaDoQuocienteDesmembrado - 9

    noveFora = [[divisor,resultado],
                [divisor*resultado+resto,decomposicaoNroDividendo]]

    print("Tabela em forma de cruz feita na folha passando como matriz para"
          "a tela a prova dos nove-fora : ",noveFora)

    resultProvaDosNove = decomposicaoNroDividendo
    return "Resultado final : ",resultProvaDosNove

#Chamando a função

print(novesFora())
