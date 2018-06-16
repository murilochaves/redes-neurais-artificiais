from manipularArquivo import *
from topologia import *

def kohonen():

    '''
    Essa função tem objetivo executar o algoritmo do Kohonen passo a passo chamando todas as outras funções em arquivos
    distintos, facilitando assima a manutenabilidade.
    '''

    #1 - Obter o conjunto de amostras de treinamento
    dataset = montarDataset('dataset/amostras_treinamento.txt')

    #2 - Definir o mapa topológico da rede
    qtdNeuronios = 16
    qtdConexoes = len(dataset[0]) # neste caso será 3

    mapa = Mapa(qtdNeuronios, qtdConexoes)

    mapa.setBidimensional()
    
    mapa.imprimirTopologia()

    dicionario_mapa = mapa.criarDicionario()

    imprimeDicionario(dicionario_mapa)

    #3 - Iniciar o Vetor de pesos de cada neurônio
    mapa.iniciarPesos_randomicamente()

    #4 - Montar o conjunto de vizinhança
    conjunto_vizinhanca = mapa.getVizinhos(1)

    dicionario_vizinhanca = criarDicionario_vizinhos(conjunto_vizinhanca)

#kohonen()