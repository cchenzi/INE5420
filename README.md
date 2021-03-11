# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

Os detalhes sobre as implementações passadas estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.4: Clipping e preenchimento de polígonos

* O sistema foi adaptado para suportar o `clipping` de objetos no mundo. Para isso, foi fixado, como solicitado, um retângulo vermelho com proporções menores que as do Canvas utilizados (20px). Atualmente, o sistema suporta o `clipping` para pontos, linhas e polígonos. Como o sistema utiliza Sistema de Coordenadas Normalizado, o `clipping` se baseou nos limites de [-1, 1], em ambos os sentidos. Os algoritmos estão no arquivo `app/clipping.py`. Um selecionador de configuração de `clipping` foi inserido na parte inferior esquerda da interface.
    - Para linhas, foram implementados os algoritmos de `Cohen-Sutherland` e `Liang-Barsky`.
    - Para polígonos, foi implementado o algoritmo `Weiler-Atherton`.

* Para facilitar a verificação, além da opção por selecionar entre os dois algoritmos de linha, foi adicionado a opção `no-clipping`, com intuito de permitir a observação do "vazamento" de pontos/linhas para fora do retângulo fixado. **Sempre** que um algoritmo de linha é selecionado, automaticamente são ligados os algoritmos de clipping de pontos e polígonos.

* Foram adicionados 6 novos exemplos de arquivos `.obj` para facilitar a verificação, também. A navegação (cima, baixo, esquerda, direita) é encorajada.
    - `clipping_points_example.obj`: possui pontos em diversas localizações da window, dentro e fora do retângulo de referência.
    - `clipping_line_example.obj`: possui um conjunto de linhas com diversos tipos de intersecções com bordas e vazamentos.
    - `wireframe_clipping_{0-4}.obj`: polígono de exemplo, transladado e rotacionado para as quatro intersecções principais do retângulo de referência. É interessante abrir os quatro ao mesmo tempo, ligar e desligar o `clipping`.


* Foi adicionada a opção de preencher o polígono com cor, no momento de sua criação. 

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



