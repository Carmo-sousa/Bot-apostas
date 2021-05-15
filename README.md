# Bot do telegram

![Autor](https://img.shields.io/badge/Sousa-Bot%20de%20apostas-yellowgreen)
![Github License](https://img.shields.io/badge/license-MIT-green)

![Logo](./img/logo.svg)

O bot envia mensagens para um chat quando algumas condições forem atendidas

## Tipos de mensagens

### Oportunidade em escanteios

Envia uma mensagem quando o apm for maior ou igual a 1.0 e a chance de gol for maior ou igual a 15.

### Oportunidade em gol

Envia uma mensagem quando o APM for maior que 1.3 e a chance de gol for maior que 15.

## Configurando o ambiente

1. Ter o python 3.8 ou superior
2. Configurar corretamente as variáveis de ambiente

    ```.env
    TELEGRAM_TOKEN=your_telegram_token
    BASE_API_URL=https://lv.scorebing.com/ajax/score/data
    CHAT_ID=your_chat_id
    ```

3. Rodar o comando `pip install -r requirements.txt` dentro da pasta do projeto.
4. Rodar o comando `python3 app.py` ou `python app.py`
5. Entrar no chat do [Bot](https://t.me/score_bing_bot)

> Se quiser gerar um novo token basta ir no [BotFather](https://t.me/BotFather) e criar um novo bot.
> Depois do token gerado basta ir nas variáveis de ambiente e trocar pelo novo token
