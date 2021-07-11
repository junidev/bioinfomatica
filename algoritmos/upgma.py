from Bio import SeqIO
import numpy as np
import sys
import numpy as np
import collections
import newick

#s1 = sys.argv[1]
#s2 = sys.argv[2]
matriz_txt = sys.argv[1]
labels = sys.argv[2]



fileVariable = open('./static/output/upgma.txt', 'r+')
fileVariable.truncate(0)
fileVariable.close()



def find_lowest(table):
  min = float("inf")
  x, y = -1, -1
  for i in range(len(table)):
    for j in range(len(table[i])):
      if table[i][j] < min:
        min = table[i][j]
        x, y = i, j
  return x, y

def SWAP(a,b):
  if b < a:
    a, b = b, a

def list_labels(labels, a, b):
  SWAP(a,b)
  labels[a] = "(" + labels[a] + "," + labels[b] + ")"
  del labels[b]

def average_jtable(table, a, b):
  if b < a:
    a, b = b, a
  row = []
  for i in range(0, a):
    row.append((table[a][i] + table[b][i])/2)
  table[a] = row
    
  for i in range(a+1, b):
    table[i][a] = (table[i][a]+table[b][i])/2
        
  for i in range(b+1, len(table)):
    table[i][a] = (table[i][a]+table[i][b])/2
    del table[i][b]
  del table[b]

def UPGMA(table, labels):
  while len(labels) > 1:
    x, y = find_lowest(table)
    average_jtable(table, x, y)
    list_labels(labels, x, y)
  return labels[0]

def make_labels(start, end):
  labels = []
  for i in range(ord(start), ord(end)+1):
    labels.append(chr(i))
  return labels


#
#0
#19
#27 31 
#8 18 26
#33 36 41 31
#18 1 32 17 35
#13 13 29 14 28 12
#


#lee el texto y convierte en matriz
def readMatrix(path):
    with open(path, 'r') as f:
        l = [[float(num) for num in line.split(' ')] for line in f]
    return l

def getLowerTriangle(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(i):
            result[i].append(matrix[i][j])
    #print(result)
    return result

def stringToList(labels):
    l = labels.split('-')
    return make_labels(l[0], l[1])

matriz = readMatrix(matriz_txt)
lower_triangle = getLowerTriangle(matriz)
M_labels = stringToList(labels)

result = UPGMA(lower_triangle,M_labels)
print(result)

tree = newick.loads(result)[0]
print(tree.ascii_art())

exit()
