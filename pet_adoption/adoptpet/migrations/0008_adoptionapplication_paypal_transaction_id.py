# Generated by Django 5.0.3 on 2024-04-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptpet', '0007_adoptionapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionapplication',
            name='paypal_transaction_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
