# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

A maneira de rodar mudou (por causa da adição de testes)! Além disso, os detalhes sobre a implementação da 1.1 estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.2: Implementação de Transformações 2D e Coordenadas Homogêneas

**Funcionalidades Implementadas:**

* Foi adicionado um novo botão, `Transform`, que abre uma janela de diálogo referente ao objeto selecionado no `display file`.

* A janela de transformações consta com 4 abas: `Rotation`, `Translation`, `Scaling` e `Reflection`, além da lista de transformações do objeto. O objeto é atualizado visualmente a cada transformação adicionada.

    - `Rotation`: é possível selecionar entre os três tipos: ao redor do centro, origem e de um ponto arbitrário.
    - `Translation`: definir (x, y).
    - `Scaling`: definir (x, y).
    - `Reflection`: escolher entre X, Y e origem.

* As matrizes de transformações estão definidas em `app/math_functions.py`, cada qual com exemplo de saída. Internamente, definimos códigos para traduzir as transformações e ser possível realizar os cálculos.

* `Wireframes` agora possuem um conjunto de coordenadas homogêneas, de coordenadas transformadas e de transformações. A função que calcula as transformações está em `app/wireframe.py`: `transform_coordinates`.

    - Coordenadas homogêneas são utilizadas nos cálculos das transformações.
    - Coordenadas transformadas são as que passaram pelas transformações e serão mostrada em tela.
    - A função `transform_coordinates` itera sobre as coordenadas homogêneas, aplicando todas as transformações e atualizando-se. Casos que precisam de translação são tratados ali mesmo. (Uma versão simplificada dessa função consta em `apply_transformations_to_points`, utilizada para testar apenas as transformações)

* Foram adicionados testes para alguns aspectos do programa. Em `tests/test_wiframe.py` são testados os exercícios de transformações (1.2.2).


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



