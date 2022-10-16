import decimal
from django.db import models

from transaction_types.models import TransactionType

# Create your models here.
class Transaction(models.Model):
    date        = models.DateField()
    value       = models.DecimalField(decimal_places=6, max_digits=7)
    cpf         = models.CharField(max_length=11)
    card_number = models.CharField(max_length=12)
    time        = models.TimeField()
    owner       = models.CharField(max_length=14)
    store       = models.CharField(max_length=19)
    tr_type     = models.ForeignKey('transaction_types.TransactionType', on_delete=models.SET_NULL, null=True)
