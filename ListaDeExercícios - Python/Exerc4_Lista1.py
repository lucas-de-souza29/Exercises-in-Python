

def sequencia():
    #Declaração de variáveis e inicialização por exemplo i =0
    lista = []
    i = 0
    nroElementos = (int(input("Informe a quantidade de elementos para a lista :")))

    while i < nroElementos:
        novoElemento = (int(input("Informe um valor : ")))
        lista.append(novoElemento)
        i+=1

    listaOrdenada = lista.copy()
    listaOrdenada.sort()
    print("Lista Normal e Lista ordenada",lista,listaOrdenada)

    cont = 0
    for j in range(0,nroElementos):

        if(listaOrdenada == lista):
           cont += 1
        else:
             print("Não são consecutivos!")
             return None

        if(cont == lista[0]-1) or (cont == lista[1]-1) or (cont == lista[2]-1):
           return True

    return False

print(sequencia())
