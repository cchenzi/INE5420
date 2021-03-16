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



## Versão 1.3: Implementação de Rotação da Window, SCN, leitura e escrita de arquivos obj

* O sistema de coordenadas foi alterado para a utilização do Sistema de Coordenadas Normalizado. Para isto, foram feitas as seguintes modificações:
    - A window foi fixada entre [-1, 1].
    - Criação da função `build_window_normalizations` (`app/math_functions`), que realiza a criação das matrizes de translação ao centro da window, a rotação do ângulo inserido e o escalonamento para a normalização. As matrizes, portanto, são compostas e retornadas. Elas são recalculadas sempre que necessário, mas apenas uma vez, pelo controlador da `main_window`. Sendo assim, cada `wireframe` recebe pronta a matriz com as transformações de window.
    - Na parte de transformações de coordenadas dos `wireframes` (`transform_coordinates` em `app/wireframe.py`), é feito um passo antes de compor as matrizes de transformações, multiplicando as coordenadas originais e homogêneas pela matriz de normalização da window. As coordenadas normalizadas e transformadas são salvas e utilizadas no desenho.

* Para a rotação da window, foi habilitado o botão de rotação "⮏", que irá girar para a esquerda o valor de graus informado (para a direita, basta inverter o sinal). Com isso, fará que recalcule a matriz de normalização, assim como as funções de navegação normais (que estão funcionando!!).

* Para lidar com arquivos `.obj`, foram criadas duas classes: `ObjLoader` e `ObjWriter`(`app/obj_handler`), além de serem adicionados dois botões: `Save` e `Load`.
    - `Load`: carrega os objetos de um aquivo obj para a cena. Caso um arquivo obj especifique um `.mtl`, é preciso que ele se encontre na mesma pasta do obj. 
    - `Save`: exporta todos os `wireframes` para um arquivo obj com o nome especificado para a cena, criando um arquivo `.mtl` auxiliar para salvar as cores dos objetos. Como as coordenadas transformadas estão normalizadas, é necessário realizar um passo de desnormalização para salvá-las. Para isso, cria-se uma matriz de normalização inversa e aplica-se as coordenadas normalizadas.

* Três arquivos foram disponibilizados, na pasta `/obj`, como exemplo de carregamento e exportação de `.obj`: `house.obj`, `pentagram.obj` e `ruby.obj`, todos eles criados e exportados pelo próprio programa.

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