import os
import re
import random

from nonebot import on_command
from datetime import datetime
import pytz

import hoshino
from hoshino import R, Service, priv, util
from hoshino.typing import CQEvent

tz = pytz.timezone('Asia/Shanghai')

sv_help = '''
原批滚出去
'''.strip()

sv = Service(
    name = 'antiyp',  #功能名
    use_priv = priv.NORMAL, #使用权限
    manage_priv = priv.SUPERUSER, #管理权限
    visible = False, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = '通用', #属于哪一类
    help_ = sv_help #帮助文本
    )

#@sv.on_keyword(('原神', '刻晴', '可莉', '派蒙', '凝光', '八重', '神子', '申鹤', '宵宫',
#     '云堇','提瓦特'))
#async def chat_sad(bot, ev):
#    await bot.send(ev, '我焯，有○批')

@sv.on_keyword(('原神', '刻晴', '可莉', '派蒙', '凝光', '八重', '神子', '申鹤', '宵宫',
     '云堇','提瓦特','芭芭拉','七七','甘雨','雷电将军','魈','香菱','行秋','重云','砂糖','莫娜','凯亚','丽莎','雷泽','温迪','北斗','安柏'
                ,'迪卢克','班尼特','菲谢尔','诺埃尔','神里绫人','埃洛伊','早柚','九条裟罗','枫原万叶','五郎','达达利亚','珊瑚宫心海'))
async def chat_sad(bot, ev):
    path = '/home/qqbot/HoshinoBot/haru-bot-setup-master/hoshino/modules/antiyp/yp/'
    ypimg = random.choice(os.listdir(path))
    msg = f'○批滚出去\n'
    try:
        ypimg = R.img(f'{ypimg}').cqcode
        msg += str(ypimg)
    except Exception as e:
        hoshino.logger.error(f'读取反原批的图片时发生错误{type(e)}')
    await bot.send(ev, msg, at_sender=True)
    await util.silence(ev, 60)