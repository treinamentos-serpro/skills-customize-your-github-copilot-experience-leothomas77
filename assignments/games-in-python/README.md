
# 📘 Assignment: Hangman Game

## 🎯 Objetivo

Construa um jogo da forca em Python para praticar strings, condicionais, loops e seleção aleatória. O jogador deverá descobrir uma palavra escolhida aleatoriamente antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Implemente a lógica principal da forca

#### Descrição
Crie uma versão jogável da forca no terminal. O programa deve escolher uma palavra de uma lista predefinida, exibir seu progresso e encerrar a rodada quando o jogador vencer ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Exibir cada letra ainda não descoberta como um sublinhado, mantendo as posições das letras e separando-as para facilitar a leitura.
- Solicitar um palpite por vez e revelar todas as ocorrências da letra quando ela estiver na palavra.
- Reduzir o número de tentativas restantes quando o palpite não estiver na palavra.
- Encerrar a rodada quando todas as letras forem descobertas ou quando não houver mais tentativas.
- Exibir uma mensagem de vitória ao descobrir a palavra e, em caso de derrota, revelar a palavra correta.

### 🛠️ Valide os palpites e permita outra partida

#### Descrição
Valide os palpites para evitar entradas inválidas ou repetidas e permita que o jogador inicie outra rodada sem reiniciar o programa.

#### Requisitos
O programa concluído deve:

- Tratar letras maiúsculas e minúsculas como o mesmo palpite.
- Rejeitar entradas vazias ou que não contenham exatamente uma letra, sem consumir uma tentativa.
- Avisar quando uma letra já tiver sido informada e não consumir uma tentativa nesse caso.
- Perguntar ao jogador se deseja iniciar outra rodada após o fim da atual.
- Ao iniciar outra rodada, selecionar uma palavra e reiniciar os palpites e o número de tentativas.
