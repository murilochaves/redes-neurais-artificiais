from neuronio import *
from math import sqrt

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
        
        print('\n### Topologia %s definida ###' % self.topologia)
        print('\n\t Qtd. Neurônios:', self.qtdNeuronios)

        if self.topologia == 'Unidimensional':
            print('\t Tam. Vetor:', len(self.neuronios))
            print('\n', self.neuronios)
            
        elif self.topologia == 'Bidimensional':
            print('\t Tam Matriz:', len(self.neuronios), 'x', len(self.neuronios[0]))
            print('\n', self.neuronios)

        else:
            print('ERRO: O mapa não tem uma topologia definida no momento')


##################
##### TESTES #####
##################

qtdNeuronios = 16
qtdConexoes = 3

mapa = Mapa(qtdNeuronios, qtdConexoes)

#mapa.setUnidimensional()
mapa.setBidimensional()