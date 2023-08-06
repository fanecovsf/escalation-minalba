# Documentação dos Endpoints da API Minalba

Este README fornece uma explicação detalhada sobre a funcionalidade de cada endpoint na API Minalba. A API Minalba disponibiliza endpoints para gerenciar informações sobre unidades e contatos dentro da organização.

## URL Base

`https://escalation-minalba.onrender.com`

## Tecnologias utilizadas
- Python
- Flask
- SQLAlchemy
- PostgreSQL

## Tratamento de Erros

A API Minalba inclui tratamento de erros tanto para os códigos de status 404 (Não Encontrado) quanto para os códigos de status 500 (Erro Interno do Servidor).

## Endpoints

### 1. GET /minalba/unidades

Este endpoint recupera uma lista de todas as unidades na organização Minalba, juntamente com seus contatos.

**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`

```json
{
    "id": 1,
    "nome": "Unidade A",
    "contatos": [
        {
            "id": 1,
            "nome": "João",
            "cargo": "Gerente",
            "nivel": "Nível 1",
            "turno": "Manhã",
            "email": "joao@example.com",
            "telefone": "123-456-7890"
        },
    ]
},
```

### 2. GET /minalba/unidades/<int:id>

Este endpoint recupera informações detalhadas sobre uma unidade específica com base no seu ID.

**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`


### 3. PUT /minalba/unidades/add

Este endpoint permite adicionar uma nova unidade à organização Minalba.

**Corpo da Requisição**
```json
{
    "nome": "Nova Unidade"
}
```


### 4. GET /minalba/contatos

Este endpoint recupera uma lista de todos os contatos na organização Minalba, incluindo suas unidades associadas.

**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`
```json
[
   {
      "id":1,
      "nome":"João",
      "cargo":"Gerente",
      "nivel":"Nível 1",
      "turno":"Manhã",
      "email":"joao@example.com",
      "telefone":"123-456-7890",
      "unidade":{
         "id":1,
         "nome":"Unidade A"
      }
   },
   "..."
]
```


### 5. GET /minalba/contatos/<int:id>

Este endpoint recupera informações detalhadas sobre um contato específico com base no seu ID.

**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`

```json
{
    "id": 1,
    "nome": "João",
    "cargo": "Gerente",
    "nivel": "Nível 1",
    "turno": "Manhã",
    "email": "joao@example.com",
    "telefone": "123-456-7890",
    "unidade": {
        "id": 1,
        "nome": "Unidade A"
    }
}
```

### 6. PUT /minalba/contatos/add

Este endpoint permite adicionar um novo contato à organização Minalba.

**Corpo da Requisição**
```json
{
    "nome": "Novo Contato",
    "cargo": "Analista",
    "nivel": "Nível 2",
    "turno": "Tarde",
    "email": "contato@example.com",
    "telefone": "987-654-3210",
    "unidade_id": 1
}
```
**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`
 

### 7. DELETE /minalba/(unidades & contatos)/delete

Este endpoint permite deletar um contato ou uma unidade apenas passando o ID do mesmo e enviando uma requisição do tipo "DELETE".

**Exemplo de Corpo da Requisição**
```json
{
    "id": 2
}
```

**Resposta**
- Código de Status: 200 (OK)
- Tipo de Conteúdo: `application/json`


## Como Utilizar

1. Realize requisições HTTP para os endpoints apropriados utilizando ferramentas como curl, Postman ou sua biblioteca de cliente HTTP preferida.
2. Siga as estruturas de requisição e resposta fornecidas para cada endpoint.


## Autor
Gustavo Henrique Faneco

`https://github.com/fanecovsf`
