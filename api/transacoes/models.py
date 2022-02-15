from datetime import datetime
from django.db import models

class Transaction(models.Model):
    INPUT_TRANSACTION = 'e'
    OUTPUT_TRANSACTION = 's'

    TYPE_TRANSACTION = (
        (INPUT_TRANSACTION, 'Entrada'),
        (OUTPUT_TRANSACTION, 'Saída')
    )
    
    title = models.CharField('Título da transação:', max_length=100, blank=False, null=False)
    amount = models.DecimalField('Preço:', max_digits=8, decimal_places=2, blank=False, null=False, default=0)
    tag = models.CharField('Tag da transação', max_length=30, blank=False, null=False)
    date = models.DateField('Data da transação', blank=False, null=False, auto_now_add=True)
    type = models.CharField('Tipo da transação', max_length=1, choices=TYPE_TRANSACTION, default=INPUT_TRANSACTION)
    
    
    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"
        ordering = ['-date']
        
        
    def __str__(self):
        return self.title
    