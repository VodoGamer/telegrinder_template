"""simple dispatch"""
from telegrinder import Dispatch, Message
from telegrinder.bot.rules import Text

from src.bot.init import api
from src.db.models import User

dp = Dispatch()


@dp.message(Text("/start"))
async def start(message: Message):
    me = (await api.get_me()).unwrap()
    user = await User.get_or_none(id=message.from_user.id)
    await message.answer(f"Hello, {user or message.from_user.username}, I am {me.first_name} bot!")
