# Generated by Django 4.0.2 on 2022-02-15 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='value_money',
            new_name='amount',
        ),
    ]