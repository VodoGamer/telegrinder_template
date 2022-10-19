"""bot init"""
import logging

from telegrinder import API, Telegrinder, Token

from src.config.env import BOT_TOKEN

logger = logging.getLogger("bot")
logging.basicConfig(level=logging.DEBUG)
api = API(token=Token(BOT_TOKEN))
bot = Telegrinder(api)
