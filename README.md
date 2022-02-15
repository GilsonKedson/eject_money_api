# API EJECT MONEY (Transações)

Repositório criado com finalidade de ajudar no desenvolvimento da trilha React JS da EJECT, fornecendo uma API simples utilizando Django Rest Framework.

## Status
Em desenvolvimento, porém utilizável. 🚧

## Endpoints HEROKU
<ul>
  <li>(<strong>GET</strong>) https://eject-money.herokuapp.com/transacoes/</li>
  <li>(<strong>POST</strong>) https://eject-money.herokuapp.com/transacoes/</li>
  <li>(<strong>GET</strong>) https://eject-money.herokuapp.com/transacoes/{id}/</li>
  <li>(<strong>PUT</strong>) https://eject-money.herokuapp.com/transacoes/{id}/</li>
  <li>(<strong>PATCH</strong>) https://eject-money.herokuapp.com/transacoes/{id}/</li>
  <li>(<strong>DELETE</strong>) https://eject-money.herokuapp.com/transacoes/{id}/</li>
</ul>

## Endpoints LOCAL
<ul>
  <li>(<strong>GET</strong>) http://127.0.0.1:8000/transacoes/</li>
  <li>(<strong>POST</strong>) http://127.0.0.1:8000/transacoes/</li>
  <li>(<strong>GET</strong>) http://127.0.0.1:8000/transacoes/{id}/</li>
  <li>(<strong>PUT</strong>) http://127.0.0.1:8000/transacoes/{id}/</li>
  <li>(<strong>PATCH</strong>) http://127.0.0.1:8000/transacoes/{id}/</li>
  <li>(<strong>DELETE</strong>) http://127.0.0.1:8000/transacoes/{id}/</li>
</ul>

## Estrutura de dados
```
(GET) https://eject-money.herokuapp.com/transacoes/

{
    "transactions": [
        {
            "id": number,
            "title": string,
            "amount": number,
            "tag": string,
            "date": string,
            "type": string
        }
    ],
    "inputs_amount": number,
    "outputs_amount": number,
    "total_amount": number
}
```

```
(GET) https://eject-money.herokuapp.com/transacoes/{id}/

{
    "id": number,
    "title": string,
    "amount": number,
    "tag": string,
    "date": string,
    "type": string
}
```

```
(POST) https://eject-money.herokuapp.com/transacoes/

Ex:

{
    "title": "Pagamento de terceirizados",
    "amount": 300,
    "tag": "Despesas",
    "type": "s"
}
```

```
(PUT OU PATCH) https://eject-money.herokuapp.com/transacoes/{id}/

Ex:

{
    "title": "Pagamento de terceirizados",
    "amount": 300,
    "tag": "Despesas",
    "type": "s"
}
```

```
(DELETE) https://eject-money.herokuapp.com/transacoes/{id}/
```
