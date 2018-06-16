from neuronio import *
from math import sqrt
from random import random

class Mapa:

    '''
    Classe de Mapa tem como objetivo a modificação facilitada da topologia do mapa
    É passado como parâmetro a quantidade de neurônios desejados juntamente com a quantidade de entrada para a criação
    dos neurônios, não tem resposta somente modifica a topologia

    ex: mapa = Mapa(qtdNeuronios, qtdConexoes)
    '''

    def __init__(self, qtdNeuronios, qtdConexoes):
        self.qtdNeuronios = qtdNeuronios
        self.qtdConexoes = qtdConexoes
        self.neuronios = []
        self.topologia = None

    def setQtdNeuronios(self, qtdNeuronios):
        self.qtdNeuronios = qtdNeuronios

    def setQtdConexoes(self, qtdConexoes):
        self.qtdConexoes = qtdConexoes

    def setTopologia(self, topologia=None):
        self.topologia = topologia

    def getQtdNeuronios(self):
        return self.qtdNeuronios

    def getQtdConexoes(self):
        return self.qtdConexoes

    def getTopologia(self):
        return self.topologia

    def getNeuronios(self):
        return self.neuronios

    def setUnidimensional(self):

        '''
        Essa função tem objetivo setar a topologia dos neurônios para um vetor
        '''

        self.neuronios = []
        self.topologia = 'Unidimensional'

        contador = 1 
        for i in range(1, self.qtdNeuronios + 1):
            self.neuronios.append(Neuronio(self.qtdConexoes, contador))
            contador += 1

        self.imprimeInfoMapa()

    def setBidimensional(self):
        
        '''
        Essa função tem como objetivo setar a topologia dos neurônios para uma matriz quadrada
        '''

        self.neuronios = []
        self.topologia = 'Bidimensional'

        tamanho = int(sqrt(self.qtdNeuronios))
        lx, ly = tamanho, tamanho
        
        contador = 1
        for i in range(lx):
            self.neuronios.append([])
            for j in range(ly):
                self.neuronios[i].append(Neuronio(self.qtdConexoes, contador))
                contador += 1

        self.imprimeInfoMapa()

    def imprimeInfoMapa(self):

        '''
        Essa função tem como objetivo apenas de imprimir as informações sobre o mapa criado
        '''
        
        print('\n### Mapas auto-organizáveis de Kohonen ###')
        print('\n\t Topologia: %s ' % self.getTopologia())
        print('\t', self.getQtdNeuronios(), ' Neurônios')
        print('\t', self.getQtdConexoes(), ' Conexões de entrada')
        #print('\n\t Qtd. Neurônios:', self.getQtdNeuronios())

        if self.topologia == 'Unidimensional':
            print('\t Tam. Vetor:', len(self.getNeuronios()), 'posições')
            print('\n', self.getNeuronios())
            
        elif self.topologia == 'Bidimensional':
            print('\t Tam Matriz:', len(self.neuronios), 'x', len(self.neuronios[0]))
            print('\n', self.getNeuronios())

        else:
            print('ERRO: O mapa não tem uma topologia definida no momento')

    def imprimirTopologia(self):
        
        '''
        Essa função tem objetivo apenas de mostrar em forma visual a topologia de como ficou o mapa dos neurônios
        '''

        print('\n### Imprimindo topologia da Rede ###')

        if self.topologia == 'Unidimensional':
            self.imprimeTopUnidimensional()

        elif self.topologia == 'Bidimensional':
            self.imprimeTopBidimensional()

       
    def imprimeTopUnidimensional(self):
        
        aux = []

        for i in range(1, len(self.neuronios) + 1):
            aux.append(i)

        print(aux)

    def imprimeTopBidimensional(self):
        
        aux = []

        contador = 1
        
        for i in range(len(self.neuronios)):
            aux.append([])
            for j in range(len(self.neuronios[0])):
                aux[i].append(contador)
                contador += 1

        for i in range(len(aux)):
            print(aux[i])
        
    def criarDicionario(self):

        '''
        Essa função tem como objetivo criar um dicionário para facilitar a manipulação dos objetos neurônios, é passado o mapa e 
        é retornado o dicionário com os id's respectivas

        Ex: dicionario_mapa = criarDicionario_Mapa(mapa)
        '''
        
        dicionario_mapa = {}

        if self.topologia == 'Unidimensional':
            dicionario_mapa = self.criaDictUnidimensional()

        if self.topologia == 'Bidimensional':
            dicionario_mapa = self.criaDictBidimensional()

        return dicionario_mapa

    def criaDictUnidimensional(self):
        
        dicionario_mapa = {}

        contador = 1

        for i in range(len(self.neuronios)):
            dicionario_mapa[contador] = self.neuronios[i]
            contador += 1

        return dicionario_mapa
    
    def criaDictBidimensional(self):
        
        dicionario_mapa = {}

        contador = 1

        for i in range(len(self.neuronios)):
            for j in range(len(self.neuronios[0])):
                # adicionar um novo valor funciona da forma: dicionario[chave] = valor do conteúdo
                dicionario_mapa[contador] = self.neuronios[i][j]
                contador += 1

        return dicionario_mapa

    def iniciarPesos_randomicamente(self):
        '''
        Essa função tem como objetivo a iniciar os pesos da rede randomicamente, não tem resultado ela só executará alterando

        Ex: inicia_pesos(mapa)
        '''

        print('\n### Iniciando Pesos randomicamente ###')

        for i in range(len(self.neuronios)):
            for j in range(len(self.neuronios[0])):
                for k in range(len(self.neuronios[i][j].w)):
                    self.neuronios[i][j].w[k] = random()
                print('Neurônio:', self.neuronios[i][j].nome, '\t', self.neuronios[i][j])
                print(self.neuronios[i][j].w, '\n')

    def getVizinhos(self, R = 0):

        '''
        Essa funçnao tem como objetivo percorrer uma matriz de neurônios e montar um vetor com o conjunto de vizinhaça
        É passada como argumento uma matriz dos neurônios juntamente com o raio e como resposta é retornado um vetor com
        a matriz de vizinhança.

        Ex: vizinhança = getVizinhos(matriz, R)
        '''
        
        vizinhanca = []

        for i in range(len(self.neuronios)):
            for j in range(len(self.neuronios[0])):
                aux = retornaVizinhos_bi_qrd_fausett(i, j, self.neuronios, R)
                #aux.append(vizinhos(i, j, matriz, R))
                vizinhanca.append(aux)
                    
        return vizinhanca

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


##################
##### TESTES #####
##################
'''
qtdNeuronios = 16
qtdConexoes = 3

mapa = Mapa(qtdNeuronios, qtdConexoes)

#mapa.setUnidimensional()
mapa.setBidimensional()
'''