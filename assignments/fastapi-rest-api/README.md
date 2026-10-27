# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para um catálogo de livros usando FastAPI. Você vai praticar rotas HTTP, validação de dados, códigos de status e respostas para recursos inexistentes.

## 📝 Tasks

### 🛠️ Listar livros

#### Descrição
Use o scaffold fornecido para criar uma API FastAPI. Implemente uma rota que retorne todos os livros cadastrados e execute a aplicação localmente. Instale as dependências com `python -m pip install "fastapi[standard]"` e inicie o servidor a partir desta pasta com `fastapi dev starter-code.py`.

#### Requisitos
O programa concluído deve:

- Criar a aplicação FastAPI com o título `School Library API`
- Implementar `GET /books` e retornar todos os livros como uma lista JSON
- Iniciar sem erros e exibir a documentação interativa em `/docs`


### 🛠️ Buscar um livro por ID

#### Descrição
Adicione uma rota para consultar um único livro pelo seu ID. Responda com um erro HTTP apropriado quando o ID não corresponder a nenhum livro.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}`
- Retornar o objeto do livro solicitado quando ele existir
- Retornar status `404` quando o livro não existir


### 🛠️ Cadastrar livros com validação

#### Descrição
Implemente a criação de livros. Use o modelo Pydantic `BookInput` do scaffold para validar o corpo da requisição e gere um novo ID para cada livro cadastrado.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` com um corpo JSON contendo `title`, `author` e `publication_year`
- Rejeitar dados inválidos usando a validação automática do FastAPI e Pydantic
- Adicionar o novo livro ao catálogo e retornar o livro criado com status `201`

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "publication_year": 1937
}
```


### 🛠️ Atualizar e remover livros

#### Descrição
Complete a API permitindo substituir os dados de um livro existente e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir os campos do livro usando `BookInput`
- Retornar o livro atualizado e status `200` após uma atualização bem-sucedida
- Implementar `DELETE /books/{book_id}` e retornar status `204` após a remoção
- Retornar status `404` ao tentar atualizar ou remover um ID inexistente