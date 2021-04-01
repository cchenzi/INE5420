# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

Os detalhes sobre as implementações passadas estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.7: Objetos 3D e Projação Paralela Ortogonal

* Para esta tarefa, atualizamos a classe `Wireframe` para suportar pontos, linhas e objetos 3D. Desse modo, tudo que for inserido, na verdade, é tratado como 3D: objetos 2D são objetos 3D com y = 0, definido como padrão na tela de inserção. Para isso, todas as funções que geram matrizes de transformações (translação, escalonamento e rotação) foram atualizadas para 3D (`app/math_functions`). No caso da rotação, gera-se três matrizes e retorna a composição delas.

* A Projeção Paralela Ortogonal está funcionando depois das alterações mencionadas. Além disso, tivemos que adaptar o leitor de arquivos `.obj`. Assim, para agrupamentos, definidos por "g", eles compõem um objeto adicional chamado `WireframeGroup`, responsável por centralizar as transformações. A definição de múltiplos "o" por arquivo ainda é permitida.

* Foram adicionados diversos exemplos na pasta `obj/3d`. retirados mo dodle da disciplina e dos seguintes sites: [https://people.sc.fsu.edu/~jburkardt/data/obj/obj.html] e [http://paulbourke.net/dataformats/obj/]. Não produzimos nenhum 3D. Os objetos 2D ainda funcionam normalmente.

* A **transformação** de rotação ao redor do centro do objeto está com problemas. Entretanto, o resto funciona normalmente.

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



