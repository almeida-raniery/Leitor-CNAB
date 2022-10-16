from enum import unique
from django.db import models


class TransactionSign(models.TextChoices):
    PLUS = "+"
    MINUS = "-"


class TransactionType(models.Model):
    description = models.CharField(max_length=24, unique=True)
    nature = models.CharField(max_length=8)
    sign = models.CharField(
        max_length=1, choices=TransactionSign.choices, default=TransactionSign.PLUS)

    def __str__(self):
        return f'{self.id} - {self.description}'
