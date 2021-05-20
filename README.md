# Bot do telegram

![Autor](https://img.shields.io/badge/Sousa-Bot%20de%20apostas-yellowgreen)
![Github License](https://img.shields.io/badge/license-MIT-green)

![Logo](./img/logo.svg)

O bot verificas os jogos ao vivos do [ScoreGing](https://www.scorebing.com/) e envia uma mensagem
no telegram quando as condições forem atendidas

## Tipos de mensagens

- Oportunidade em escanteios

Envia uma mensagem quando o APM(ataque por minuto) for maior ou igual a 1.0 e a chance de gol for maior ou igual a 15.

- Oportunidade em gol

Envia uma mensagem quando o APM(Ataque por minuto) for maior que 1.3 e a chance de gol for maior que 15.

## Configurando o ambiente

1. Python 3.6 ou superior
2. Configurar corretamente as variáveis de ambiente

    ```.env
    TELEGRAM_TOKEN=<Telegram_token>
    BASE_API_URL=https://lv.scorebing.com/ajax/score/data
    CHAT_ID=<your_chat_id>
    ```

3. Executar o comando `pip install -r requirements.txt` dentro da pasta do projeto. *Se estiver em um ambiente linux use `pip3`.*
4. Executar o comando `python3 app.py` no linux ou `python app.py` no windows
5. Entrar no chat do [Bot](https://t.me/score_bing_bot)

> Para gerar um token basta ir no [BotFather](https://t.me/BotFather) e criar um novo bot.
> Depois do token gerado basta ir nas variáveis de ambiente e trocar pelo novo token
