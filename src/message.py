from telegram import Bot

def mount_message(
    type_message,
    league,
    status,
    team_h,
    goals_h,
    goals_g,
    team_g,
    on_target,
    off_garget,
    danger_attack,
    corners,
    possessions_h,
    possessions_g,
    apm,
    opportunity_goals,
):
    message = f"""
    <b>{type_message}:</b>
    {league}
    {team_h} {goals_h} X {goals_g} {team_g}

    {danger_attack} ataques perigosos em {status} minútos.
    {on_target} chutes a gol.
    {off_garget} chutes fora.
    {corners} cantos (escanteios).

    Posse de bola {possessions_h} x {possessions_g};

    APM = {apm: .2f};
    chance de gol = {opportunity_goals};
    """

    return message



def send_message(token, chat_id, message):
    for _ in range(1, 6):
        bot = Bot(token=token)
        bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
