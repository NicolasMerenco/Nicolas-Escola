#semana 21. Vetores empython(lista)

vector_inteiros=[1,2,3,4,5]
vector_misto=['a',2,3,True,'Python']

#Acesso a elementos do vetor. O acesso aos elemetos é feito a síntexe vetor [indice] Exemplo:

primeiro_elemento=vector_inteiros[0] #Acesso ao primeiro elemento.
terceiro_elemento=vector_inteiros [2] #Acesso ao terceiro elemento.

#Acesso negativo:
#-->Começa a contar a partir do final do vetor (-1 sendo o último elemento)

último_elemento=vector_inteiros [-1] #Acesso ao último elemento.
penúltimo_elemento=vector_inteiros [-2] #Acesso ao penúltimo elemento.
tamanho_vetor=len(vector_inteiros) #Retorna ao tamanho do elemento.

#OBS: Essa função len (vetor) é útil para laço de repetição e verificação de limite.

#Alterando elementos

vector_inteiros [0]=10 #Altere o primeiro elemento para 10.

#Percorrendo vetores - Para percorrer todos os elementos de um vetor, pode-se usar um laço FOR. Exeemplo:

for elemento in vector_inteiros:
    print(elemento) #Imprime cada elemento do vetor

#Fatiamento de vetores - O fatiamento permite obter uma sublista de um vetor usando o sistema vetor [inicio:fim]. O índice de início é inclusivo e o índice de fim é exclusivo. Exemplo:

subvetor=vector_inteiros [1:3] #Obtém uma sublista do segundo ao terceiro elemento.

#Adição de elementos - Elementos podem ser adicionados ao find de um vetor usando o método append(). Exemplo:

vector_inteiros.append(6) #Adiciona o número 6 ao final do vetor.

#Inserção de elementos - Para inserir um elemento em uma posição específica, usa-se o método insert (indice,elemento). Exemplo:

vector_inteiros.insert(2,15) #Insere o número 15 na terceira posição.

#Remoção de elementos - Elementos podem ser removidos pelo valor com remove(valor), ou pelo indice com del vetor [indice]. Exemplo:

vector_inteiros.remove (15) #Remove o número 15 do vetor
del vector_inteiros [2] #Remove o elemento no indice 2.

#List Comprehensions - É uma forma concisa de criar listas com base em listas existentes, com a possibilidade de aplicar condições e operações. Exemplo:

quadrados=[x for x in range (10)]

#Matrizes (listas de listas) - Em python uma matriz pode ser representada como uma lista de listas. Cada elemento da lista principal é uma lista da matriz, e cada um desses elementos é outra lista contendo os elementos da linha. Exemplo:

Matriz=[[1,2,3],[4,5,6],[7,8,9]] #Representa uma matriz 3x3
elemento=Matriz [1][2] #Acesso ao elemento na segunda linha, terceira coluna.

#END


