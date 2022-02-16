from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from utils.entradas import get_amount_transaction_input
from utils.saidas import get_amount_transaction_output
from utils.valores_total import total_amount

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    
    def list(self, request):
        transactions = Transaction.objects.all()
        income = Transaction.INPUT_TRANSACTION
        expense = Transaction.OUTPUT_TRANSACTION
        serializer = TransactionSerializer(transactions, many=True)
        inputs = get_amount_transaction_input(transactions.filter(type=income))
        outputs = get_amount_transaction_output(transactions.filter(type=expense))
        total_value_amount = total_amount(inputs, outputs)
        
        context = {
            'transactions': serializer.data,
            'inputs_amount': inputs,
            'outputs_amount': outputs,
            'total_amount': total_value_amount,
        }
        
        return Response(context)
    