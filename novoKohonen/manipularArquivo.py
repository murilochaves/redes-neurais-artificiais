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

    print(
    '''\n### Dataset constituído ###
        
    Qtd. de amostras: ''', len(dataset), '''
    Qtd. de grandezas: ''', len(dataset[0]), '''
    '''
    )
    print(dataset)

    return dataset

##################
##### TESTES #####
##################

#dataset = montarDataset('dir/arquivo.txt')

#print(dataset)