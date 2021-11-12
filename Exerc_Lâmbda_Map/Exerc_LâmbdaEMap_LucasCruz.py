
#Listas
pedido = ['34587','98762','77226','88112']
valorPedido = [40.95,56.80,32.95,24.99]

#Função lâmbda
# lambda x: x + 10

def lerValores():
   totalPedido = 0
   for i in (pedido):
       input("Informe o numero do pedido : ")
       for j in (valorPedido):
           input("Informe o valor do pedido : ")
           totalPedido = valorPedido
           if(totalPedido < 100):
              totalPedido = lambda valorPedido : valorPedido + 10
              resp = []
              resp.append(totalPedido,valorPedido)
   return resp

list(map(filter(lerValores())))


