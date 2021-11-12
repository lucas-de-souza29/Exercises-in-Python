

#Listas e dicionários

#A partir do dicionário 1 não pode ser feito a busca pela string por meio de erro de sintaxe!!!

# dicionario1 = {'c1':{'c1':[0,21,{c2:'oi',c4:'olá'},4]},35,'c3'}

l1 = [0,2,{'k1':[32,0,[1,2,{'k2':2,'k3':'olá'}]]}]


lista = []
lista = l1.copy()

key = ''
dic = {}

def imprimeStringOla():
    for i in range(0,len(lista)):
        key = i
        dic[key] = []
        if(i != key):
           dic[key].append(i)
           i+=1
    dic[2] = ['olá']
    print(dic)

    if 2 in dic:
        return (dic[2])

print(imprimeStringOla())







