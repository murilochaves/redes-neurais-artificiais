from math import sqrt

class Neuronio:

    '''
    Classe do neurônio de Kohonen, a unidade de processamento é peculiar, portanto difere dos outros neurônios comuns
    Temos que passar no construtor, o número de conexões que cada neurônio terá, e será criado vetor dos pesos sinápticos
    respectivos, juntamente com o ID do neurônio (para facilitar o controle)
    Também podemos setar fora do construtor e retornar os pesos
    '''

    def __init__(self, n, id):
        self.w = [0.0] * n
        self.id = id

    def setW(self, w):
        self.w = w

    def setId(self, id):
        self.id = id

    def getW(self):
        return self.w

    def getId(self):
        return self.id

def imprimeMatriz(matriz):

    '''
    Essa função tem somente a obrigação de facilitar e reutilizar o código para imprimir matriz
    
    Ex: imprimeMatriz(matriz)
    '''

    print('\n### Imprimindo matriz ###')

    for i in range(len(matriz)):
        print(matriz[i])

def imprimeMatrizFantasiosa(matriz):

    '''
    Essa função tem objetivo apenas de mostrar em forma visual a topologia de como ficou o mapa dos neurônios
    '''

    print('\n### Imprimindo topologia da Rede ###')

    aux = []

    contador = 1

    for i in range(len(matriz)):
        aux.append([])
        for j in range(len(matriz[0])):
            aux[i].append(contador)
            contador += 1

    for i in range(len(aux)):
        print(aux[i])

def montarDataset(arquivo):

    '''
    Essa função tem a obrigação de abrir arquivos e montar os datasets respectivos para reutilização de código
    É passado um caminho onde está o arquivo à ser aberto e como resposta, retorna uma matriz com os valores contidos no arquivo txt
    
    Ex: dataset = montarDataset('Kohonen/dataset/amostra_treinamento.txt')
    '''

    dataset = []

    arq_dataset = open(arquivo)

    for linha in arq_dataset:
        
        valores = linha.split()

        dataset.append(valores)

    return dataset

def criarMapa_Bidimensional(dimX, dimY, conexoes):

    '''
    Essa função tem como funcionalidade criar o mapa de neurônios bidimensional por exemplo (4x4 - 16 objetos) e como resposta,
    retorna o mapa de objetos neurônios
    '''

    mapa = []

    contador = 1

    for i in range(dimY):
        mapa.append([])
        for j in range(dimX):
            mapa[i].append(Neuronio(conexoes, '%d' % contador))
            contador += 1

    return mapa

def criarDicionario_Mapa(mapa):

    '''
    Essa função tem como objetivo criar um dicionário para facilitar a manipulação dos objetos neurônios, é passado o mapa e 
    é retornado o dicionário com os id's respectivas

    Ex: dicionario_mapa = criarDicionario_Mapa(mapa)
    '''
    
    dicionario_mapa = {}

    contador = 1

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            # adicionar um novo valor funciona da forma: dicionario[chave] = valor do conteúdo
            dicionario_mapa[contador] = mapa[i][j]
            contador += 1

    return dicionario_mapa

def imprimeDicionario(dicionario):

    '''
    Essa função tem como objetivo mostrar os respectivos neurônios e suas posições de memória
    '''

    print('\n### Dicionário dos Neurônios ###')
    
    for item in dicionario:
        print('Neurônio', item, '\t', dicionario[item])

#1 - Obter o conjunto de amostras de treinamento
dataset = montarDataset('Kohonen/dataset/amostra_treinamento.txt')

#2 - Definir o mapa topológico da rede
qtdNeuronios = 16

tamanho = int(sqrt(qtdNeuronios))
dimX, dimY = tamanho, tamanho

conexoes = len(dataset[0])

mapa = criarMapa_Bidimensional(dimX, dimY, conexoes)

dicionario_mapa = criarDicionario_Mapa(mapa)

print(
'''
\n### Mapas auto-organizáveis de Kohonen ###

    ''', qtdNeuronios, ''' Neurônios
    ''', conexoes, ''' Conexões de Xn
    ''', dimX, 'x', dimY, ''' Matriz'''

    )

imprimeMatrizFantasiosa(mapa)

imprimeDicionario(dicionario_mapa)

#3 - Iniciar o Vetor de pesos de cada neurônio




# Inicializar pesos w_ij // para isso, temos que saber a 


# dataset possui 3 grandezas então teremos 3 conexões para cada neurônio {x1, x2, x3}

# contituir a rede com 16 neurônios (4x4)

# treinar com taxa de aprendizado de 0,001

# vizinhança unitário R = 1
