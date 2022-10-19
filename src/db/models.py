"""simple tortoise-orm model"""
from tortoise import fields
from tortoise.models import Model


class User(Model):
    id: int = fields.IntField(pk=True)
    name: str = fields.CharField(255)

    def __str__(self) -> str:
        return self.name
