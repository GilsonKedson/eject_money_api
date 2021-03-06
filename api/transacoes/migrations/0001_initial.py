# Generated by Django 4.0.2 on 2022-02-14 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título da transação:')),
                ('value_money', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Preço:')),
                ('tag', models.CharField(max_length=30, verbose_name='Tag da transação')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data da transação')),
                ('type', models.CharField(choices=[('e', 'Entrada'), ('s', 'Saída')], default='e', max_length=1, verbose_name='Tipo da transação')),
            ],
            options={
                'verbose_name': 'Transação',
                'verbose_name_plural': 'Transações',
                'ordering': ['-date'],
            },
        ),
    ]
