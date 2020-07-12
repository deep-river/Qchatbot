from nonebot import on_command, CommandSession, get_bot
from time import time
from config import TIMELASPE, CONTENT


bot = get_bot()
bot.content_timestamp = -TIMELASPE


@on_command('content', aliases=('UNSIGNED'))
async def content(session: CommandSession):
    timestamp = time()
    if timestamp - bot.content_timestamp >= TIMELASPE:
        await session.send(CONTENT)
        bot.content_timestamp = timestamp
