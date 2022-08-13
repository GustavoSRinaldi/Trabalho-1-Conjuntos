#Gustavo Sampietro Rinaldi - Trabalho 1 Conjuntos

def U(): #União, checa as variáveis que não estão em R2
  global R2
  for i in (data[a]+data[b]):
    if i not in R2:
      R2.append(i)
  R2 = ",".join(R2)
  
def I(): #Interseção, checa as variáveis que estão em ambos conjuntos
  global R2
  for i in data[a]:
    if i in data[b]:
      R2.append(i)
  R2 = ",".join(R2)

def D(): #Diferença, checa as variáveis que estão no conjunto 1 e não estão no conjunto 2
  global R2
  for i in data[a]:
    if i not in data[b]:
      R2.append(i)
  R2 = ",".join(R2)

def C(): #Cartesiano, multiplica todos os números do conjunto 1 pelos do conjunto 2
  global R2
  for i in range (len(data[a])):
    for j in range (len(data[b])):
      A = data[a][i]+data[b][j]
      R2.append(A)
  R2 = ",".join(R2)

f = open("file1.txt","r")

data = []

#coloca os valores do txt dentro de uma matriz
for line in f:
  data.append(line.strip().split(","))

f.close()

#variavéis que deixam o código dinâmico
Loop = int(data[0][0])
a = 2
b = 3
c = 1

while Loop > 0:
  #váriaveis para o print
  C1 = ",".join(data[a])
  C2 = ",".join(data[b])  
  R2=[]
  #define qual operação será feita
  Operation = data[c]
  if Operation == ['U']:
    OP = "União"
    U()
  elif Operation == ['I']:
    OP = "Interseção"
    I()
  elif Operation == ['D']:
    OP = "Diferença"
    D()
  elif Operation == ['C']:
    OP = "Cartesiano"
    C()
  else:
    print("\nOperação inválida\n")
    break
  #formatação do print
  print (f'{OP}: conjunto 1',' {',C1,'}, conjunto 2 {',C2,'}. Resultado:{',R2,'}',sep='')
  #atualiza as variáveis dinâmicas
  Loop -= 1
  a += 3
  b += 3
  c += 3