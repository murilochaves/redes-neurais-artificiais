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