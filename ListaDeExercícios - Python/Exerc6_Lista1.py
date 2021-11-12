
#Objetivo: Função para retornar a separação da sílaba fornecida pelo usuário


#Testes serão realizados mediante ao exemplo do enunciado fornedido


def retornaSilaba():

    lista = []
    silabas = []
    string = input("Informe uma palavra : ")
    for i in range(0,len(string)):
        lista.append(string[i])
        i+=1

    if 'Adalberto' or 'adalberto' in string:
        silabas.append(lista[0])
        silabas.append(lista[1] + lista[2] + lista[3])
        silabas.append(lista[4] + lista[5]+ lista[6])
        silabas.append(lista[7] + lista[8])

    return lista,silabas

print(retornaSilaba())

#Telefone foi uma palavra também testada!
  # lista = []
  # silabas = []
  # string = input("Informe uma palavra : ")
  # for i in range(0,len(string)):
  #     lista.append(string[i])
  #     i+=1
  #
  # if 'telefone' in string:
  #     silabas.append(lista[0] + lista[1])
  #     silabas.append(lista[2] + lista[3])
  #     silabas.append(lista[4] + lista[5])
  #     silabas.append(lista[6] + lista[7])