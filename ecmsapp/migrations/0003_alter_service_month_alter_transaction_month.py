# Generated by Django 4.1.7 on 2023-05-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecmsapp', '0002_service_month_service_process_transaction_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='month',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='month',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
