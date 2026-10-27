# 📘 Assignment: Persistent Book Catalog with JSON

## 🎯 Objective

Adapte um catálogo de livros para salvar e carregar seus dados em um arquivo JSON. Você vai praticar persistência usando os módulos `json` e `pathlib`, que fazem parte da biblioteca padrão do Python.

## 📝 Tasks

### 🛠️ Save the Catalog to a JSON File

#### Description
Implemente a função `save_books(books)` para gravar a lista de livros no arquivo `books.json` ao lado do código inicial.

#### Requirements
O programa concluído deve:

- Usar `json.dump()` para salvar a lista em formato JSON
- Abrir o arquivo com codificação UTF-8 e usar indentação para facilitar a leitura
- Criar ou substituir `books.json` ao salvar

### 🛠️ Load the Catalog from a JSON File

#### Description
Implemente `load_books()` para ler `books.json` e retornar a lista de livros salva.

#### Requirements
O programa concluído deve:

- Usar `json.load()` para ler os dados do arquivo
- Retornar a lista de livros, mantendo os campos e valores salvos
- Demonstrar que os livros carregados correspondem aos que foram salvos

### 🛠️ Keep New Books Between Runs

#### Description
Complete `main()` para carregar o catálogo existente ou começar com os livros de exemplo quando o arquivo ainda não existir. Depois, permita adicionar um livro e salve o catálogo atualizado.

#### Requirements
O programa concluído deve:

- Carregar `books.json` quando o arquivo existir e usar `INITIAL_BOOKS` na primeira execução
- Pedir título, autor e ano de publicação para um novo livro
- Adicionar o livro ao catálogo e salvar a lista atualizada
- Manter o novo livro no catálogo depois de fechar e executar o programa novamente