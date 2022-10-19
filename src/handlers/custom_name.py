"""simple dispatch with tortoise-orm"""
from telegrinder import Dispatch, Message
from telegrinder.bot.rules import Markup

from src.db.models import User

dp = Dispatch()


@dp.message(Markup("/setname <new_name>"))
async def setname(message: Message, new_name: str):
    await User.update_or_create({"name": new_name}, id=message.from_user.id)
    await message.answer("Your name has been updated!")
