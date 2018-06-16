from random import random
from math import sqrt

class Neuronio:

    '''
    Classe do neurônio de Kohonen, a unidade de processamento é peculiar, portanto difere dos outros neurônios comuns
    Temos que passar no construtor, o número de conexões que cada neurônio terá, e será criado vetor dos pesos sinápticos
    respectivos, juntamente com o ID do neurônio (para facilitar o controle)
    Também podemos setar fora do construtor e retornar os pesos
    '''

    def __init__(self, n, nome = None):
        self.w = [0.0] * n
        self.nome = nome

    def setW(self, w):
        self.w = w

    def setNome(self, nome):
        self.nome = nome

    def getW(self):
        return self.w

    def getNome(self):
        return self.nome

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

def criarDicionario_vizinhos(conjunto_vizinhanca):

    '''
    Essa função tem como objetivo criar um dicionário para facilitar a visualização do conjunto de vizinhança dos neurônios
    é passado o vetor montado do conjunto de vizinhança e é retornado o dicionário com as posições
    '''

    dicionario_vizinhos = {}

    contador = 1

    for i in range(len(conjunto_vizinhanca)):
        # adicionar um novo valor funciona da forma: dicionario[chave] = valor do conteúdo
        dicionario_vizinhos[contador] = conjunto_vizinhanca[i]
        contador += 1

    print('\n### Imprimindo o conjunto de vizinhança dos neurônios ###')

    for item in dicionario_vizinhos:
        print('Neurônio:', item, '\n', dicionario_vizinhos[item], '\n')

    return dicionario_vizinhos

def imprimeDicionario(dicionario):

    '''
    Essa função tem como objetivo mostrar os respectivos neurônios e suas posições de memória
    '''

    print('\n### Dicionário dos Neurônios ###')
    
    for item in dicionario:
        print('Neurônio', item, '\t', dicionario[item])

def inicia_pesos(mapa):

    '''
    Essa função tem como objetivo a iniciar os pesos da rede randomicamente, não tem resultado ela só executará alterando

    Ex: inicia_pesos(mapa)
    '''

    print('\n### Iniciando Pesos randomicamente ###')

    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            for k in range(len(mapa[i][j].w)):
                mapa[i][j].w[k] = random()
            print('Neurônio:', mapa[i][j].nome, '\t', mapa[i][j])
            print(mapa[i][j].w, '\n')

def retornaVizinhos_bi_qrd_fausett(linha, coluna, matriz, R):

    '''
    Essa função tem como objetivo retornar os vizinhos específicos de um nó utilizando a topologia bidimensional quadrada
    e vizinhança proposta por fausett
    É passada a localização exata do nó em uma matriz (linha, coluna), passada também a matriz específica junto com R que seria o Raio
    como resposta, é retornado um vetor com os nós respectivos.
    '''

    vizinhos = []
    
    if R < 0:
        R = 0

    while R >= len(matriz) or R >= len(matriz[0]):
        R = R - 1

    #linha = linha
    #coluna = coluna
    
    #print('\nLinha: ', linha)
    #print('Coluna: ', coluna)

    linhaInicial = linha - R
    linhaFinal = linha + R
    
    if linhaInicial < 0:
        linhaInicial = 0
    while linhaFinal > len(matriz)-1:
        linhaFinal = linhaFinal - 1

    #print('\nLinhaInicial: ', linhaInicial)
    #print('LinhaFinal: ', linhaFinal)

    colunaInicial = coluna - R
    colunaFinal = coluna + R
    
    if colunaInicial < 0:
        colunaInicial = 0
    while colunaFinal > len(matriz[0])-1:
        colunaFinal = colunaFinal - 1

    #print('\nColunaInicial: ', colunaInicial)
    #print('colunaFinal: ', colunaFinal, '\n')
    
    for i in range(linhaInicial, linhaFinal+1):
        for j in range(colunaInicial, colunaFinal+1):
            if R == 0:
                vizinhos.append(matriz[i][j])
            if R != 0 and matriz[i][j] != matriz[linha][coluna]:
                vizinhos.append(matriz[i][j])
            #vizinhos.append(matriz[i][j])

    return vizinhos

def getVizinhos(matriz, R):

    '''
    Essa funçnao tem como objetivo percorrer uma matriz de neurônios e montar um vetor com o conjunto de vizinhaça
    É passada como argumento uma matriz dos neurônios juntamente com o raio e como resposta é retornado um vetor com
    a matriz de vizinhança.

    Ex: vizinhança = getVizinhos(matriz, R)
    '''
    
    vizinhanca = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            aux = retornaVizinhos_bi_qrd_fausett(i, j, matriz, R)
            #aux.append(vizinhos(i, j, matriz, R))
            vizinhanca.append(aux)
                
    return vizinhanca

#   #   #   #   #   #   #   #   #   #

#1 - Obter o conjunto de amostras de treinamento
dataset = montarDataset('dataset/amostra_treinamento.txt')

print(dataset)

#   #   #   #   #   #   #   #   #   #

#2 - Definir o mapa topológico da rede
qtdNeuronios = 16

tamanho = int(sqrt(qtdNeuronios))
dimX, dimY = tamanho, tamanho

conexoes = len(dataset[0])

mapa = criarMapa_Bidimensional(dimX, dimY, conexoes)

dicionario_mapa = criarDicionario_Mapa(mapa)

print('''\n### Mapas auto-organizáveis de Kohonen ###

    ''', qtdNeuronios, ''' Neurônios
    ''', conexoes, ''' Conexões de x (entradas)
    ''', dimX, 'x', dimY, ''' Matriz'''

    )

imprimeMatrizFantasiosa(mapa)

imprimeDicionario(dicionario_mapa)

#   #   #   #   #   #   #   #   #   #

#3 - Iniciar o Vetor de pesos de cada neurônio
inicia_pesos(mapa)

#   #   #   #   #   #   #   #   #   #

#4 - Montar o conjunto de Vizinhança
R = 1

conjunto_vizinhanca = getVizinhos(mapa, R)

dicionario_vizinhanca = criarDicionario_vizinhos(conjunto_vizinhanca)

# treinar com taxa de aprendizado de 0,001