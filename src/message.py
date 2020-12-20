from telegram import Bot


def mount_message(major, minor, type_message, league, status):
    message = f"""
<b>{type_message}: {major.name}</b>
{league}
{major.name} {major.goals} x {minor.goals} {minor.name}

{major.danger_attack} ataques perigosos em {status} minútos.
{major.on_target} chutes a gol.
{major.off_garget} chutes fora.
{major.corners} cantos (escanteios).

Posse de bola {major.possession} x {minor.possession};

APM: {major.apm_minute: .2f};
chance de gol: {major.opportunity_goals};
""".replace(
        ".", ","
    )
    return message


def send_message(token, chat_id, message):
    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
