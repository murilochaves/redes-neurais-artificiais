## 3.6 - Projeto Prático

<div align='justify'>
  <p>
    Pela análise de um processo de destilação fracionada de petróleo observou-se que determinado óleo poderia ser classificado em duas classes de pureza <code>{<i>P<sub>1</sub> e P<sub>2</sub></i>}</code> a partir da medição de três grandezas <code>{<i>x<sub>1</sub>, x<sub>2</sub> e x<sub>3</sub></i>}</code>, que representam algumas de suas propriedades físico-químicas. A equipe de engenheiros e cientistas pretende usar uma rede <i>Perceptron</i> para executar a classificação automática das duas classes.
  <p>
  
  <p>
    Assim, baseado nas informações coletadas do processo, formou-se o conjunto de treinamento apresentado no <LINK DO CONJUNTO DE TREINAMENTO>, tomando por convenção o valor `-1` para óleo pertencente à classe `P1` e o valor `1` para óleo pertencente à classe `P2`.

Para tanto, o <b>neurônio</b> constituinte do <i>Perceptron</i> terá então <b>três entradas</b> e <b>uma saída</b> conforme ilustrado na imagem:

<FOTO>

Legenda: Arquitetura do <i>Perceptron</i> para o projeto prático.

Utilizando o algoritmo supervisionado de `Hebb` (<i>regra de Hebb</i>) para <b>classificação de padrões</b>, e assumindo-se a taxa de aprendizagem como `0,01`, faça as seguintes atividades:

1. Execute <b>cinco treinamentos</b> para a rede <i>Perceptron</i>, iniciando o vetor de pesos `{w}` em <b>cada treinamento com valores aleatórios entre zero e um</b>. Se for o caso, reinicie o gerador de números aleatórios em cada treinamento de tal forma que os elementos do vetor de pesos iniciais não sejam os mesmos. O conjunto de treinamento encontra-se em <LINK DO CONJUNTO DE TREINAMENTO>.

2. Registre os resultados dos cinco treinamentos na tabela:

Tabela 1 - Resultados dos treinamentos do Perceptron
<table>
  <tr>
    <th rowspan="2">Treina<br>mento</th>  <th colspan="4">Vetor de Pesos</th>  <th colspan="4">Vetor de Pesos<br>Finais</th>  <th>Número<br>de<br>Épocas</th>
  </tr>
  <tr>
    <td>w0</td> <td>w1</td> <td>w2</td> <td>w3</td> <td>w0</td> <td>w1</td> <td>w2</td> <td>w3</td> <td></td>
  </tr>
  <tr>
    <td>T1</td><td>0.4016<\td><td>0.4429<\td><td>0.44<\td><td>0.0817<\td>
               <td>1.6616<\td><td>1.4676<\td><td>2.1572<\td><td>-0.7337<\td>
               <td>161<\td>
  </tr>
  <tr>
    <td>T2</td><td>0.5278<\td><td>0.4484<\td><td>0.1016<\td><td>0.9047<\td>
               <td>1.9078<\td><td>1.3516<\td><td>1.9892<\td><td>-0.6799<\td>
               <td>160<\td>
  </tr>
  <tr>
    <td>T3</td><td>0.7506<\td><td>0.2206<\td><td>0.0162<\td><td>0.2437<\td>
               <td>2.0406<\td><td>1.2912<\td><td>1.9018<\td><td>-0.6501<\td>
               <td>155<\td>
  </tr>
  <tr>
    <td>T4</td><td>0.1111<\td><td>0.0192<\td><td>0.6143<\td><td>0.0954<\td>
               <td>1.5311<\td><td>1.5286<\td><td>2.2354<\td><td>-0.7623<\td>
               <td>158<\td>
  </tr>
  <tr>
    <td>T5</td><td>0.4376<\td><td>0.0287<\td><td>0.7302<\td><td>0.8884<\td>
               <td>1.8076<\td><td>1.3908<\td><td>2.066<\td><td>-0.7016<\td>
               <td>142<\td>
  </tr>
</table>

Após o treinamento do Perceptron, coloque este em operação, aplicando-o na classificação automática das amostras de óleo da tabela 1.2, indicando ainda nesta tabela aqueles resultados das saídas (Classes) referentes aos cinco processos de treinamento realizados no item 1.

Tabela 1.2 — Amostras de óleo para validar a rede Perceptron
<table>
  <tr>
    <th>Amostra</th><th>x1</th><th>x2</th><th>x3</th><th>Y(T1)</th><th>Y(T2)</th><th>Y(T3)</th><th>Y(T4)</th><th>Y(T5)</th> </tr>
  <tr>
    <td>1</td><td>-0,3665</td><td>0,0620</td><td>5,9891</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td>
  </tr>
  <tr>
    <td>2</td><td>-0,7842</td><td>1,1267</td><td>5,5912</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>3</td><td>0,3012</td><td>0,5611</td><td>5,8234</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>4</td><td>0,7757</td><td>1,0648</td><td>8,0677</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>5</td><td>0,1570</td><td>0,8028</td><td>6,3040</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>6</td><td>-0,7014</td><td>1,0316</td><td>3,6005</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>7</td><td>0,3748</td><td>0,1536</td><td>6,1537</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td>
  </tr>
  <tr>
    <td>8</td><td>-0,6920</td><td>0,9404</td><td>4,4058</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
  <tr>
    <td>9</td><td>-1,3970</td><td>0,7141</td><td>4,9263</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td>
  </tr>
  <tr>
    <td>10</td><td>-1,8842 </td><td>0,2805</td><td>1,2548</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td><td>+1</td>
  </tr>
</table>

Explique por que o número de épocas de treinamento , em relação a esta aplicação, varia cada vez que executamos o treinamento do Perceptron.

Para a aplicação em questão, discorra se é possível afirmar se as suas classes são linearmente separáveis.

Conjunto de treinamento

(Exercício do livro: Redes neurais artificiais para engenharia e ciências aplicadas pg. 70-72)

</div>
