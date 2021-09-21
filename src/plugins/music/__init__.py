from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from . import data_source
qqmusic = on_command("点歌", priority=5)

@qqmusic.handle()
async def handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = str(event.get_message()).strip()
    msg = ''  
    if args !='':
        id =await data_source.qq_search(args)
        if id != '':
            msg='[CQ:music,type=qq,id={}]'.format(id)
    Msg = Message(msg)
    await qqmusic.finish(Msg)

music = on_command("网易点歌", priority=5)

@music.handle()
async def handle(bot: Bot, event: GroupMessageEvent, state: T_State):
    args = str(event.get_message()).strip()
    msg = ''  
    if args !='':
        id =await data_source.neteasy_search(args)
        if id != '':
            msg='[CQ:music,type=163,id={}]'.format(id)
    Msg = Message(msg)
    await music.finish(Msg)

