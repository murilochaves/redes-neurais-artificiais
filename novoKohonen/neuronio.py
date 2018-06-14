class Neuronio:

    '''
    Classe do neurônio de Kohonen, a unidade de processamento é peculiar, portanto difere dos outros neurônios comuns
    Temos que passar no construtor, o número de conexões que cada neurônio terá, e será criado vetor dos pesos sinápticos
    respectivos, juntamente com o ID do neurônio (para facilitar o controle)
    Também podemos setar fora do construtor e retornar os pesos
    '''

    def __init__(self, n, nome=None):
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
