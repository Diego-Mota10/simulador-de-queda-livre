# Simulador de Queda Livre

Simulador interativo de queda livre desenvolvido em **Python** utilizando a biblioteca **Pygame**.

O programa permite simular a queda de uma maçã sob diferentes acelerações gravitacionais, representando a gravidade de diferentes corpos do Sistema Solar.

## Sobre o projeto

O objetivo deste projeto é utilizar programação para representar computacionalmente um problema de Física: o movimento de um corpo em queda livre.

A maçã inicia sua queda a partir de uma altura de **2 metros** e o usuário pode selecionar diferentes corpos celestes para observar como a aceleração da gravidade influencia o tempo de queda.

A simulação utiliza a aceleração gravitacional correspondente ao corpo selecionado e atualiza o movimento da maçã ao longo do tempo.

## Funcionalidades

* Simulação de queda livre;
* Altura inicial de 2 metros;
* Seleção da aceleração gravitacional;
* Simulação em diferentes corpos do Sistema Solar;
* Cronômetro para medir o tempo de queda;
* Representação gráfica do movimento;
* Controle da simulação pelo teclado.

## Corpos disponíveis

O usuário pode selecionar:

| Tecla | Corpo    |
| ----- | -------- |
| `0`   | Sol      |
| `1`   | Mercúrio |
| `2`   | Vênus    |
| `3`   | Terra    |
| `4`   | Lua      |
| `5`   | Marte    |
| `6`   | Júpiter  |
| `7`   | Saturno  |
| `8`   | Urano    |
| `9`   | Netuno   |

## Como utilizar

1. Execute o programa.
2. Selecione um corpo celeste utilizando as teclas de `0` a `9`.
3. Pressione **Espaço** para iniciar a queda.
4. Observe o movimento da maçã e o tempo decorrido.

A seleção do corpo celeste deve ser realizada antes de iniciar a simulação.

## Física utilizada

Para uma queda livre partindo do repouso, a posição do corpo pode ser descrita por:

$$
\Delta y = \frac{1}{2}gt^2
$$

onde:

* \(\Delta y\) é o deslocamento vertical;
* \(g\) é a aceleração gravitacional;
* \(t\) é o tempo de queda.

O tempo teórico de queda pode ser obtido por:

$$
t = \sqrt{\frac{2h}{g}}
$$

Neste projeto, a altura inicial utilizada é:

$$
h = 2\,m
$$

Assim, diferentes valores de \(g\) produzem diferentes tempos de queda.

## Implementação da cinemática

Para transformar as equações da cinemática em uma simulação visual, foi necessário estabelecer uma relação entre as unidades físicas e os pixels da tela.

A maçã utilizada na simulação possui **30 pixels de altura**, sendo utilizada como referência para estabelecer a escala entre a representação gráfica e as grandezas físicas.

A posição da maçã é armazenada em pixels, enquanto o movimento é atualizado utilizando o intervalo de tempo `dt`, obtido a partir do relógio do Pygame:

```python
dt = clock.tick(120) / 1000
```

Dessa forma, `dt` representa o intervalo de tempo, em segundos, transcorrido entre duas atualizações consecutivas da simulação.

A velocidade e a posição são então atualizadas a cada ciclo:

```python
self.vely += self.acely * dt
self.posy += self.vely * dt
```

Essas atualizações correspondem, numericamente, às relações:

$$
v(t+\Delta t) = v(t) + a\Delta t
$$

e

$$
y(t+\Delta t) = y(t) + v\Delta t
$$

A aceleração utilizada é determinada pela gravidade do corpo celeste selecionado.

### Conversão entre pixels e metros

Para representar uma altura física na tela, foi estabelecida uma escala de conversão entre pixels e metros. A dimensão conhecida da maçã, de **30 pixels**, foi utilizada como referência para essa construção.

Assim, a posição visual da maçã pode ser relacionada à sua posição física por meio de uma relação de escala:

$$
y_{\text{metros}} = \frac{y_{\text{pixels}}}{\text{pixels por metro}}
$$

Essa abordagem permite que a animação visual represente um movimento com grandezas físicas definidas, em vez de apenas deslocar a imagem pela tela.


## Tecnologias utilizadas

* **Python**
* **Pygame**

## Estrutura do projeto

```text
.
├── main.py
├── Maca.py
├── planeta.py
├── relogio.py
├── maca.png
├── demonstracao.gif
└── README.md
```

### `main.py`

Responsável pelo funcionamento principal da aplicação, incluindo:

* criação da janela;
* gerenciamento dos eventos do teclado;
* seleção do corpo celeste;
* atualização da simulação;
* exibição das informações na tela.

### `Maca.py`

Contém a classe responsável pela maçã e pelo seu movimento.

A classe controla:

* posição;
* velocidade;
* aceleração;
* movimento;
* atualização da posição na tela.

### `planeta.py`

Armazena os valores de aceleração gravitacional utilizados na simulação.

### `relogio.py`

Responsável pelo controle do tempo utilizado na simulação.

## Demonstração

![Demonstração do simulador](demonstracao.gif)

## Objetivo do projeto

Este projeto foi desenvolvido como uma aplicação prática para estudar a integração entre **programação e modelagem física**.

Além de praticar Python e Pygame, o projeto busca representar conceitos de cinemática por meio de uma simulação computacional interativa.

## Próximos passos

Algumas melhorias planejadas para versões futuras:

* Permitir que o usuário escolha a altura inicial;
* Exibir a altura atual da maçã;
* Exibir a velocidade instantânea;
* Comparar o tempo experimental da simulação com o tempo teórico;
* Adicionar gráficos de posição e velocidade;
* Melhorar a interface gráfica;
* Permitir a alteração da velocidade inicial;
* Adicionar outras situações de movimento.

## Autor

**Diego**
