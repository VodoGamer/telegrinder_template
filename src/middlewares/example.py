"""simple middleware"""
from typing import Any

from telegrinder import ABCMiddleware, Message


class ExampleMiddleware(ABCMiddleware):
    async def pre(self, event: Message, ctx: dict):
        return None

    async def post(self, event: Message, responses: list[Any], ctx: dict):
        return None
