from nonebot import get_bot
from time import time
from config import GROUPLIST, USERLIST, AUTOREPLY, TIMELASPE, CONTENT

# 监听特定群聊中特定用户发言，并自动回复
bot = get_bot()
message_count = len(AUTOREPLY)

bot.message_counter = 0
bot.reply_timestamp = -TIMELASPE


@bot.on_message('group')
async def handle_group_message(ctx):
    group_id = ctx['group_id']
    user_id = ctx['sender']['user_id']
    if group_id in GROUPLIST and user_id in USERLIST:
        timestamp = time()
        # print("proceed --> ")
        # bot.message_counter == 0 and timestamp - bot.reply_timestamp < time_lapse --> won't proceed
        if bot.message_counter != 0 or timestamp - bot.reply_timestamp >= TIMELASPE:
            message_num = bot.message_counter % message_count
            await bot.send_group_msg(group_id=group_id, message=AUTOREPLY[message_num])
            bot.message_counter += 1
            if bot.message_counter == message_count:
                bot.message_counter = 0
            if bot.message_counter == 1:
                bot.reply_timestamp = timestamp

