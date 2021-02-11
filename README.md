# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Versão 1.1: Sistema Básico com Window e Viewport

**Funcionalidades Implementadas:**

* Os objetos são definidos como `wireframes` (`wireframe.py`), tendo seu tipo decidido dinamicamente através do enum `Shape` (`utils.py`). `Wireframes` possuem nome, tipo, lista de coordenadas, número de pontos e cor de exibição.

* A tela principal apresenta as funcionalidades do Sistema Básico. À esquerda, está localizada a lista de objetos e botões para manipulação.
    - `Add`: abre uma nova janela para a criação de um novo `wireframe`. Nesta janela, é necessário informar os pontos desejados. Também é possível selecionar a cor de exibição.
    - `Delete`: deleta o `wireframe` selecionado na lista de objetos.
    - `Clear`: deleta todos os `wireframes` da lista de objetos.
    - `Refresh`: reseta os parâmetros de navegação e redesenha os objetos na tela.

* Ainda à esquerda, estão disponíveos os botões de navegação 2D e zoom, com `step` previamente definidos:
    - `Navegação 2D`: esquerda, direita, cima e baixo.
    - `Zoom`: in e out.

* A tela de criação de `wirefame` apresenta os botões:
    - `Add`: adiciona o ponto (X, Y) descrito no campo de texto acima.
    - `Delete`: deleta o ponto selecionado da lista de pontos à direita.
    - `Pick Color`: selecionar cor de exibição do `wireframe`.
    - `Draw`: desenha o `wireframe` no canvas.

## Execução

A única dependência direta consiste na biblioteca `PyQt5`.

### Com poetry

Utilizamos `Poetry` para gerenciar dependências e ambientes. Para executar o projeto localmente, as dependências podem ser instaladas utilizando o `Poetry`. Caso não possua ele instalado, o [tutorial da documentação do Poetry](https://python-poetry.org/docs/) pode ser seguido.
Tendo o Poetry instalado, basta rodar o seguinte comando para instalar as dependências:

`poetry install`

É necessário ainda o pacote do `Qt`, ferramenta utilizada para o desenvolvimento da interface. Instruções de como instalá-lo em diversas distribuições podem ser encontradas na [Qt Wiki](https://wiki.qt.io/Main).

O projeto pode ser executado com ajuda do _makefile_ com o comando `make app`, e os testes podem ser rodados com `make test`.

### Sem poetry

Para executar sem a ajuda do __makefile__ e do `poetry`, basta rodar com

`python3 app/main.py`

atentando-se com as dependências necessárias.



