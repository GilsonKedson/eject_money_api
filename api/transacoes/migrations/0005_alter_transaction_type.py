# Generated by Django 4.0.2 on 2022-02-16 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0004_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('income', 'Entrada'), ('expense', 'Saída')], default='income', max_length=7, verbose_name='Tipo da transação'),
        ),
    ]