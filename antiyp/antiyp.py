import os
import random
import aiohttp
from hoshino import R, Service, util
from hoshino.config import RES_DIR

sv = Service('antiyp', help_='原批滚出去')

antiyp = os.path.join(os.path.expanduser(RES_DIR), 'img', 'yp')

@sv.on_keyword(('原神','刻晴','可莉','派蒙','凝光','八重','神子','申鹤','宵宫','云堇'))
async def qks_keyword(bot, ev):
   yp = random.choice(os.listdir(antiyp))
    msg = f'○批滚出去\n'
    try:
        ypimg = R.img(f'antiyp/{ypimg}').cqcode
        msg += str(ypimg)
    except Exception as e:
        hoshino.logger.error(f'读取反原神的图片时发生错误{type(e)}')
    await bot.send(ev, msg, at_sender=True)
    await util.silence(ev, 60)