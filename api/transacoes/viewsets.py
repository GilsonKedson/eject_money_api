from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from utils.entradas import get_money_transaction_input
from utils.saidas import get_money_transaction_output
from utils.valores_total import total_money

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    
    def list(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        inputs = get_money_transaction_input(transactions.filter(type='e'))
        outputs = get_money_transaction_output(transactions.filter(type='s'))
        total_value_money = total_money(inputs, outputs)
        
        context = {
            'transactions': serializer.data,
            'inputs_money': inputs,
            'outputs_money': outputs,
            'total_money': total_value_money,
        }
        
        return Response(context)
    