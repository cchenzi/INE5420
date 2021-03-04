# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

Os detalhes sobre as implementações passadas estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.3: Implementação de Rotação da Window, SCN, leitura e escrita de arquivos obj

**Funcionalidades Implementadas:**

* O sistema de coordenadas foi alterado para a utilização do Sistema de Coordenadas Normalizado. Para isto, foram feitas as seguintes modificações:
    - A window foi fixada entre [-1, 1].
    - Criação da função `build_window_normalizations` (`app/math_functions`), que realiza a criação das matrizes de translação ao centro da window, a rotação do ângulo inserido e o escalonamento para a normalização. As matrizes, portanto, são compostas e retornadas. Elas são recalculadas sempre que necessário, mas apenas uma vez, pelo controlador da `main_window`. Sendo assim, cada `wireframe` recebe pronta a matriz com as transformações de window.
    - Na parte de transformações de coordenadas dos `wireframes` (`transform_coordinates` em `app/wireframe.py`), é feito um passo antes de compor as matrizes de transformações, multiplicando as coordenadas originais e homogêneas pela matriz de normalização da window. As coordenadas normalizadas e transformadas são salvas e utilizadas no desenho.

* Para a rotação da window, foi habilitado o botão de rotação "⮏", que irá girar para a esquerda o valor de graus informado (para a direita, basta inverter o sinal). Com isso, fará que recalcule a matriz de normalização, assim como as funções de navegação normais (que estão funcionando!!).

* Para lidar com arquivos `.obj`, foram criadas duas classes: `ObjLoader` e `ObjWriter`(`app/obj_handler`), além de serem adicionados dois botões: `Save` e `Load`.
    - `Load`: carrega os objetos de um aquivo obj para a cena. Caso um arquivo obj especifique um `.mtl`, é preciso que ele se encontre na mesma pasta do obj. 
    - `Save`: exporta todos os `wireframes` para um arquivo obj com o nome especificado para a cena, criando um arquivo `.mtl` auxiliar para salvar as cores dos objetos. Como as coordenadas transformadas estão normalizadas, é necessário realizar um passo de desnormalização para salvá-las. Para isso, cria-se uma matriz de normalização inversa e aplica-se as coordenadas normalizadas.

* Três arquivos foram disponibilizados, na pasta `/obj`, como exemplo de carregamento e exportação de `.obj`: `house.obj`, `pentagram.obj` e `ruby.obj`, todos eles criados e exportados pelo próprio programa.

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



