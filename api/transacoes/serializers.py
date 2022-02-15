from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    
    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'tag', 'date', 'type']
        