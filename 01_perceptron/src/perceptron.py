#  -*- coding: utf-8 -*-

"""
Algorítmo Perceptron:

Entradas:
    x_i (i-ésima entrada): Reais ou Binários (advindas externamente)

Pesos sinápticos:
    w_i (associado a x_i): Reais (iniciados aleatoriamente)

Limiar:
    θ: Real (iniciado aleatoriamente)

Saída:
    y: Binária

Função de ativação:
    g(.): Degrau ou degrau bipolar

Processo de treinamento:
    Supervisionado

Regra de aprendizado:
    Regra de Hebb
"""

def treinamento_perceptron():
    """
    Algorítmo Perceptron - Fase de Treinamento.
    """

    # Início {Algoritmo Perceptron - Fase de Treinamento}
        # 1. Obter o conjunto de amostras de treinamento {x^(k)};
        # 2. Associar a saída desejada {d^(k)} para cada amostra obtida;
        # 3. Iniciar o vetor w com valores aleatórios pequenos;
        # 4. Especificar a taxa de aprendizagem {n} [0 < n < 1];
        # 5. Iniciar o contador de número de épocas {época <- 0};
        # 6. Repetir as instruções:
            # 6.1 erro <- "inexiste";
            # 6.2 Para todas as amostras de treinamento {x^(k), d^(k)}, fazer:
                # 6.2.1 u <- w^T . x^(k);
                # 6.2.2 y <- sinal(u);
                # 6.2.3 Se y != d^(k)
                    # 6.2.3.1 Então:
                        # w <- w + n . (d^(k) - y) . x^(k)
                        # erro <- "existe"
            # 6.3 época <- época + 1;
        # Até que erro = "inexiste"
    # Fim {Algoritmo Perceptron - Fase de Treinamento}

if __name__ == '__main__':
    pass
