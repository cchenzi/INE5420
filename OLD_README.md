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