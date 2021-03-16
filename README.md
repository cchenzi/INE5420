# INE5420 - Computação Gráfica

## Descrição

Este repositório contém o trabalho prático desenvolvido para a primeira parte da matéria INE5420 (Computação Gráfica) cursado no Departamento de Informática e Estatística da Universidade Federal de Santa Catarina. Ele consiste em um sistema gráfico interativo, capaz de representar, em perspectiva realista, objetos em 3D como modelos de arame e também como superfícies bicúbicas renderizadas como malhas de curvas.

## Atenção

Os detalhes sobre as implementações passadas estão no arquivo OLD_README.md. Decidimos deixar neste arquivo apenas as novidades desenvolvidas.

## Versão 1.5 - Implemente Curvas em 2D usando Blending Functions

* Nesta entrega, decidimos implementar a Curva de Bézier. Para isso:
    - adicionamos uma nova classe `BezierCurve`, que herda de `Wireframe`. Ela possui duas alterações básicas: recebe um conjunto de `base points`, que necessariamente respeita as regras de criação (tamanho 4, 7, 10...), e um método novo que cria as coordenadas baseadas nos `base points` e na `accuracy` definida. Sendo assim, é possível inserir diversas curvas em apenas um objeto `BezierCurve`, como solicitado, com continuidade G(0).
    - foi alterada a interface de criação de `wireframe`: agora, há uma nova aba destinada para a inserção de Curva de Bézier (botão `add`).
    - definimos as `blending functions` de Bézier em `app/math_functions.py`, assim como o método auxiliar para o cálculo dos pontos.
    - aplicamos o `clipping` de pontos, na função `clip` (`app/clipping.py`).

* Como sugestão de teste, criamos uma figura de um coração, composta por duas curvas de Bézier. Os pontos base, caso queiram visualizar, são (0.0, 100.0), (120.0, 200.0), (240.0, 100.0), (0.0, -100.0), para o lado direito, e (0.0, 100.0), (-120.0, 200.0), (-240.0, 100.0), (0.0, -100.0) para o esquerdo. É interessante notar que o `clipping` funciona normalmente caso alguma das extremidades seja levada para fora do retângulo, no sentido de aparecer a "volta" do objeto em tela.

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



