# Bot do telegram

O bot envia mensagens para um chat quando algumas condições forem atendidas

## Tipos de mensagens

### Oportunidade em escanteios

Envia uma mensagem quando o apm for maior ou igual a 1.0 e a chance de gol for maior ou igual a 15.

### Oportunidade em gol

Envia uma mensagem quando o APM for maior que 1.3 e a chance de gol for maior que 15.

## Configurando o ambiente

1. Ter o python 3.8 ou superior
2. Configurar corretamente as variáveis de ambiente
3. Rodar o comando `pip install -r requirements.txt` dentro da pasta do projeto.
4. Rodar o comando `python3 app.py` ou `python app.py`

> Trocar os valores entre <> pelos valores corretos.

```.env
TELEGRAM_TOKEN=<token_do_bot>
BASE_API_URL=https://lv.scorebing.com/ajax/score/data
CHAT_ID=<id_do_chat>
```
