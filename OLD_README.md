## Versão 1.2: Implementação de Transformações 2D e Coordenadas Homogêneas

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

## Versão 1.1: Sistema Básico com Window e Viewport

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