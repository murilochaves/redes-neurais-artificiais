## 3.6 - Projeto Prático

<div align='justify'>

  <p>
    Pela análise de um processo de destilação fracionada de petróleo observou-se que determinado óleo poderia ser classificado em duas classes de pureza <code>{<i>P<sub>1</sub> e P<sub>2</sub></i>}</code> a partir da medição de três grandezas <code>{<i>x<sub>1</sub>, x<sub>2</sub> e x<sub>3</sub></i>}</code>, que representam algumas de suas propriedades físico-químicas. A equipe de engenheiros e cientistas pretende usar uma rede <i>Perceptron</i> para executar a classificação automática das duas classes.
  <p>
  
  <p>
    Assim, baseado nas informações coletadas do processo, formou-se o conjunto de treinamento apresentado no <a href="https://github.com/MuriloChaves/redes-neurais-artificiais/blob/master/perceptron/dados/Tabela%23Seção3.6_RNA.txt">apêndice I<a>, tomando por convenção o valor <code><i>-1</i></code> para óleo pertencente à classe <code><i>P<sub>1</sub></i></code> e o valor <code><i>1</i></code> para óleo pertencente à classe <code><i>P<sub>2</sub></i></code>.
  <p>

  <p>
    Para tanto, o <code><i>neurônio</i></code> constituinte do <i>Perceptron</i> terá então <code><i>três entradas</i></code> e <code><i>uma saída</i></code> conforme ilustrado na <code><i>figura 3.8</i></code>:
  </p>
    
  <br>

  <div align='center'>
    <img src="https://github.com/MuriloChaves/redes-neurais-artificiais/blob/master/perceptron/imagens/estrutura_perceptron.png?raw=true" width="50%">
    <p>
      <i>Figura 3.8 - Arquitetura do Perceptron para o projeto prático.</i>
    </p>
  </div>
    
  <br>
  
  <p>
    Utilizando o <code><i>algoritmo supervisionado de Hebb</i></code> (<code><i>regra de Hebb</i></code>) para <code><i>classificação de padrões</i></code>, e assumindo-se a <code><i>taxa de aprendizagem</i></code> como <code><i>0,01</i></code>, faça as seguintes atividades:
  </p>

  <p>
    <b>1</b>. <code><i>Execute cinco treinamentos</i></code> para a rede <i>Perceptron</i>, <code><i>iniciando o vetor de pesos {<b>w</b>} em cada treinamento com valores aleatórios entre zero e um</i></code>. Se for o caso, reinicie o gerador de números aleatórios em cada treinamento de tal forma que os elementos do vetor de pesos iniciais não sejam os mesmos. O conjunto de treinamento encontra-se no <a href="https://github.com/MuriloChaves/redes-neurais-artificiais/blob/master/perceptron/dados/Tabela%23Seção3.6_RNA.txt">apêndice I<a>.
  </p>
  
  <p>
    <b>2</b>. Registre os resultados dos cinco treinamentos na <code><i>tabela 3.2</i></code> apresentada a seguir:
  </p>
    
  <br>
    
  <div align='center'>
    <p>
      <i>Tabela 3.2 - Resultados dos treinamentos do Perceptron.</i>
    </p>
    <table>
      <thead>
        <tr>
          <th rowspan="2">Treinamento</th>
          <th colspan="4">Vetor de pesos iniciais</th>
          <th colspan="4">Vetor de pesos finais</th>
          <th>Número de épocas</th>
        </tr>
        <tr>
          <td><b>w<sub>0</sub></b></code></td>
          <td><b>w<sub>1</sub></b></code></td>
          <td><b>w<sub>2</sub></b></code></td>
          <td><b>w<sub>3</sub></b></code></td>
          <td><b>w<sub>0</sub></b></code></td>
          <td><b>w<sub>1</sub></b></code></td>
          <td><b>w<sub>2</sub></b></code></td>
          <td><b>w<sub>3</sub></b></code></td>
          <td></td>
        </tr>
      </thead>
      <tbody>
        <tr align='center'>
          <td>1º (T1)</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <tr align='center'>
          <td>2º (T2)</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <tr align='center'>
          <td>3º (T3)</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <tr align='center'>
          <td>4º (T4)</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <tr align='center'>
          <td>5º (T5)</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
  </div>
  
  <br>
  
  <p>
    <b>3</b>. <code><i>Após o treinamento</i></code> do <i>Perceptron</i>, coloque este em operação, <code><i>aplicando-o na classificação automática das amostras</i></code> de óleo da <code><i>tabela 3.3</i></code>, indicando ainda nesta tabela aqueles <code><i>resultados das saídas</i></code> (Classes) <code><i>referentes aos cinco processos de treinamento realizados</i></code> no <code><i>item 1</i></code>.
  </p>
  
  <br>

  <div align='center'>
    <p>
      <i>Tabela 3.3 — Amostras de óleo para validar a rede Perceptron.</i>
    </p>
    <table>
    <thead>
      <tr>
        <th>Amostra</th>
        <th><b>x<sub>1</sub></b></th>
        <th><b>x<sub>2</sub></b></th>
        <th><b>x<sub>3</sub></b></th>
        <th><b>y</b><br>(<b>T1</b>)</th>
        <th><b>y</b><br>(<b>T2</b>)</th>
        <th><b>y</b><br>(<b>T3</b>)</th>
        <th><b>y</b><br>(<b>T4</b>)</th>
        <th><b>y</b><br>(<b>T5</b>)</th>
      </tr>
    </thead>
    <tbody>
      <tr align='center'>
        <td>1</td>
        <td>-0,3665</td>
        <td>0,0620</td>
        <td>5,9891</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>2</td>
        <td>-0,7842</td>
        <td>1,1267</td>
        <td>5,5912</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>3</td>
        <td>0,3012</td>
        <td>0,5611</td>
        <td>5,8234</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>4</td>
        <td>0,7757</td>
        <td>1,0648</td>
        <td>8,0677</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>5</td>
        <td>0,1570</td>
        <td>0,8028</td>
        <td>6,3040</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>6</td>
        <td>-0,7014</td>
        <td>1,0316</td>
        <td>3,6005</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>7</td>
        <td>0,3748</td>
        <td>0,1536</td>
        <td>6,1537</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>8</td>
        <td>-0,6920</td>
        <td>0,9404</td>
        <td>4,4058</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>9</td>
        <td>-1,3970</td>
        <td>0,7141</td>
        <td>4,9263</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr align='center'>
        <td>10</td>
        <td>-1,8842</td>
        <td>-0,2805</td>
        <td>1,2548</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
    </tbody>
    </table>
  </div>

  <br>
  
  <p>
    <b>4</b>. Explique por que o número de épocas de treinamento, em relação a esta aplicação, varia cada vez que executamos o treinamento do <i>Perceptron</i>.
  </p>

  <p>
    <b>5</b>. Para a aplicação em questão, discorra se é possível afirmar se as suas classes são linearmente separáveis.
  </p>
            
  <br>

  <div align='center'>
    <code><i>(Fonte: SILVA, Ivan Nunes da; SPATTI, Danilo Hernane; FLAUZINO, Rogério Andrade. Redes neurais artificiais para engenharia e ciências aplicadas - curso prático. 2. ed. São Paulo: Artliber, 2016. 70-72 p.)</i></code>
  </div>

</div>
