from rest_framework import serializers

from transactions.models import Transaction
from transactions.validators import validate_numeric

class TransactionSerializer(serializers.ModelSerializer):
    cpf         = serializers.CharField(validators = [validate_numeric])

    class Meta:
        model = Transaction
        fields= "__all__"
        depth=0