# Generated by Django 4.1.5 on 2023-03-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='razorpayid',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpaysignature',
            field=models.CharField(default='', max_length=255),
        ),
    ]
