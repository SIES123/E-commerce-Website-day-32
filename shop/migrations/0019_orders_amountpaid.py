# Generated by Django 4.1.5 on 2023-03-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_orders_paymentstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amountpaid',
            field=models.CharField(default='', max_length=255),
        ),
    ]
