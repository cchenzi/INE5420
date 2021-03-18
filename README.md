# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

Os detalhes sobre as implementações passadas estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.6: B-Splines utilizando Forward Differences

* Impementamos B-Splines utilizando Foward Differences. Para isso, nós criamos uma classe `Curve`, que herda de `Wireframe`. Após essa mudança, tanto `BezierCurve` como `BSplineCurve` herdam de `Curve`. Para `BSplineCurve`, existem algumas funções importantes de nota:
    - `build_curve_coordinates`: as coordenadas são criadas na própria função . Nela, é invocada a função de gerar as diferenças iniciais para cada conjunto de 4 pontos de controle e realiza as iterações necessárias para o algoritmo.
    - Em `app/math_functions.py`, estão as funções auxiliares , que retorna a matriz de B-Spline; `calculate_initial_differences`, que calcula o vetor de diferenças iniciais; `calculate_bspline_parameters`, que agrega as duas funções anteriores.
    - o `clipping` segue a mesma orientação dea entrega anterior.
    
* Mudamos a interface de criação de curvas para selecionar qual o modelo desejado, `Bezier` ou `B-Spline`. Conforme seleção, a acurácia (delta, no caso da `B-Spline`) padrão é alterada (20 para a primeira, 0.1 para a segunda). Quando inseridos no `display file`, cada curva específica tem seu nome especificado, também.

## Execução

Dependências diretas consistem nas bibliotecas `PyQt5` e `numpy`.

### Com poetry

Utilizamos `Poetry` para gerenciar dependências e ambientes. Para executar o projeto localmente, as dependências podem ser instaladas utilizando o `Poetry`. Caso não possua ele instalado, o [tutorial da documentação do Poetry](https://python-poetry.org/docs/) pode ser seguido.
Tendo o Poetry instalado, basta rodar o seguinte comando para instalar as dependências:

`poetry install`

É necessário ainda o pacote do `Qt`, ferramenta utilizada para o desenvolvimento da interface. Instruções de como instalá-lo em diversas distribuições podem ser encontradas na [Qt Wiki](https://wiki.qt.io/Main).

O projeto pode ser executado com ajuda do _makefile_ com o comando `make app`, e os testes podem ser rodados com `make test`.

### Sem poetry

Para executar sem a ajuda do __makefile__ e do `poetry`, basta rodar com

`python3 -m app`

atentando-se com as dependências necessárias.



