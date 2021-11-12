#Testes realizados com o numeros baixos( Exemplo utilizado foi o número 2)
# Resultado (MaiorPrimo = 2, QtdePrimo = 1)

def lerNro():
    divisor = 0
    qtdePrimos = 0

    nro = (int(input("Digite um numero : ")))
    for i in range (1, nro + 1):
        print("Valores de i e nro: ",i,nro)
        if(nro % i == 0):
           divisor += 1
           qtdePrimos += 1
           maiorPrimo = i
        if divisor > 2:
            print("Excedeu o limite de calculo")

    return maiorPrimo, qtdePrimos -1

print(lerNro())
