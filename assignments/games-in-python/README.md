
# 📘 Assignment: Games in Python

## 🎯 Objective

Construa um jogo da forca em Python para praticar strings, condicionais, loops e seleção aleatória. O jogador deverá descobrir uma palavra oculta antes de esgotar as tentativas.

## 📝 Tasks

### 🛠️ Implemente o jogo da forca

#### Descrição
Crie uma versão jogável da forca no terminal. O programa deve escolher uma palavra de uma lista predefinida e atualizar a exibição conforme o jogador acerta letras.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Exibir cada letra ainda não descoberta como um sublinhado, separando as posições para facilitar a leitura.
- Solicitar palpites de uma letra e revelar todas as ocorrências da letra quando ela estiver na palavra.
- Reduzir o número de tentativas restantes somente quando o palpite não estiver na palavra.
- Encerrar a partida quando a palavra for descoberta ou quando não houver mais tentativas.
- Exibir a palavra correta e uma mensagem adequada de vitória ou derrota ao final.

### 🛠️ Trate palpites repetidos e ofereça outra partida

#### Descrição
Melhore a experiência de jogo validando os palpites e permitindo que o jogador inicie uma nova partida sem reiniciar o programa.

#### Requisitos
O programa concluído deve:

- Aceitar letras maiúsculas e minúsculas sem diferenciar uma da outra.
- Rejeitar entradas vazias ou que não sejam uma única letra, sem consumir uma tentativa.
- Avisar quando uma letra já tiver sido informada e não consumir uma tentativa nesse caso.
- Perguntar ao jogador se deseja iniciar outra partida depois que uma terminar.