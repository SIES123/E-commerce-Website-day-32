# Generated by Django 4.1.5 on 2023-03-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_orders_razorpayid_orders_razorpaysignature'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='razorpaypaymentid',
            field=models.CharField(default='', max_length=255),
        ),
    ]