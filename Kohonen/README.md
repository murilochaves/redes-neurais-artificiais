# Projeto Prático

No processo industrial de fabricação de pneus sabe-se que o composto que forma a borracha pode apresentar imperfeições que impedem a sua utilização. Diversas amostras dessas anomalias foram coletadas, sendo que também foram realizadas as medidas referentes a **três grandezas**

$$ 
\{x_1, x_2, x_3\} 
$$

As quais fazem parte do processo de fabricação das respectivas borrachas. Contudo, a equipe de engenheiros  e cientistas não tem percepção técnica de como essas variáveis podem estar relacionadas.

Assim, pretende-se aplicar uma rede de Kohonen, **constituída de 16 neurônios** (figura 1), com o objetivo de detectar as eventuais similaridades e correlações existentes entre essas variáveis, pois se tem como objetivo final o posterior agrupamento das amostras imperfeitas em classes.

![enter image description here](https://lh3.googleusercontent.com/cfJWth_I9y2XeELwA3A7AVmoITY2AFA4h7vs415kS6amRiVbeHsQbIG88bQu8bPS8qWmjAIiooLL)
<center>Figura 1 - Estrutura espacial do mapa auto-organizável do projeto prático</center>

Portanto, baseado nos dados fornecidos no apêndice V, treine um mapa auto-organizável de Kohonen, conforme a estrutura espacial apresentada na Figura 1, utilizando a **taxa de aprendizado no valor de 0,001**.

O diagrama esquemático da grade bidimensional ilustrando as vizinhanças interneurônios, assumindo-se aqui um raio de **vizinhança unitário (R = 1)**, é apresentado na Figura 2.

![enter image description here](https://lh3.googleusercontent.com/utpHvMltIJivUuPFrMBn_6c1CoxHfkkOd_w6u97AhK8_qC_jCs9qgRy1-v6LL3I3WSGaafERYEt2)
<center>Figura 2 - Arranjo de vizinhança entre os neurônios (R = 1)</center>

De posse dos resultados advindos do treinamento da rede, efeutou-se uma análise neste conjunto  veerificou-se que as amostras de 1 a 20, de 21 a 60 e aquelas de 61 a 120 possuem particularidades em comum, podendo ser então consideradas **três classes** distintas, denominadas de classe *A*, *B*, *C*, respectivamente.

Por conseguinte, cabem os seguintes exercícios:

 1. Realize a identificação sobre quais os conjuntos de neurônios representados na grade da Figura 2 fornecem respostas relativas às classes *A*, *B*, *C*.
 2. Para as amostras da Tabela 1, indique a classe à qual cada uma pertence.

|Amostra|$$x_1$$|$$x_2$$|$$x_3$$|Classe|
|--|--|--|--|--|--|
|1|0.2471|0.1778|0.2905|
|2|0.8240|0.2223|0.7041|
|3|0.4960|0.7231|0.5866|
|4|0.2923|0.2041|0.2234|
|5|0.8118|0.2668|0.7484|
|6|0.4837|0.8200|0.4792|
|7|0.3248|0.2629|0.2375|
|8|0.7209|0.2116|0.7821|
|9|0.5259|0.6522|0.5957|
|10|0.2075|0.1669|0.1745|
|11|0.7830|0.3171|0.7888|
|12|0.5393|0.7510|0.5682|

> teste de comentário