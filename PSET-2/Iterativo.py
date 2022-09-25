import sys

class Pilha:
  def __init__(self, capacity):
    self.capacity = capacity
    self.top = -1
    self.array = [0]*capacity

def criarPilha(capacity):
  pilha = Pilha(capacity)
  return pilha

def cheia(pilha):
  return (pilha.top == (pilha.capacity - 1))
  
def vazia(pilha):
  return (pilha.top == -1)

def push(pilha, item):
  if(cheia(pilha)):
    return
  pilha.top+=1
  pilha.array[pilha.top] = item

def Pop(pilha):
  if(vazia(pilha)):
    return -sys.maxsize
  Top = pilha.top
  pilha.top-=1
  return pilha.array[Top]
   

def moverEntre2Torres(origem, destino, ori, dest):
    topoOrigem = Pop(origem)
    topoDestino = Pop(destino)
 
    # Quando origem está vazia
    if (topoOrigem == -sys.maxsize):
        push(origem, topoDestino)
        moverDisco(dest, ori, topoDestino)
       
    # Destino estiver vazia
    elif (topoDestino == -sys.maxsize):
        push(destino, topoOrigem)
        moverDisco(ori, dest, topoOrigem)
       
    # Topo da Origem > Destino
    elif (topoOrigem > topoDestino):
        push(origem, topoOrigem)
        push(origem, topoDestino)
        moverDisco(dest, ori, topoDestino)
       
    # Topo da Origem < Destino
    else:
        push(destino, topoDestino)
        push(destino, topoOrigem)
        moverDisco(ori, dest, topoOrigem)
   
# Função para mostrar o movimento
def moverDisco(origem, destino, disco):
    print("Mover disco", disco, "da torre", origem, "para a", destino)
   
# Função de hanoi
def hanoi(n, origem, aux, dest):
  a = "origem" 
  b = "auxiliar"
  c = "destino"

  if (n % 2 == 0):
    temp = c
    c = b
    b = temp
  t_moves = int(pow(2, n) - 1)
   
  for i in range(n, 0, -1):
    push(origem, i)
   
  for i in range(1, t_moves + 1):
    if (i % 3 == 1):
      moverEntre2Torres(origem, dest, a, c)
   
    elif (i % 3 == 2):
      moverEntre2Torres(origem, aux, a, b)
   
    elif(i % 3 == 0):
      moverEntre2Torres(aux, dest, b, c)

n = int(input("Quantos discos tem a torre?\nResposta: "))
 
# cria 3 pilhas para os discos de tamanho n
origem = criarPilha(n)
destino = criarPilha(n)
aux = criarPilha(n)
 
hanoi(n, origem, aux, destino)
 