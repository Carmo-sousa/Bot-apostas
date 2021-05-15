from typing import Union
from telegram import Bot

from score_bing.message import Message
from score_bing.team import Team

repeated: list
bot: Bot
data: Union[dict, str]
_id: str
host: Team
guest: Team
total_goals: int
corners_conditions_h: bool
corners_conditions_g: bool
goals_conditions_h: bool
goals_conditions_g: bool
message: Message
