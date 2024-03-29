# Generated by Django 5.0.3 on 2024-03-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptpet', '0002_adopt_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopt',
            name='month_year',
            field=models.CharField(choices=[('years', 'years'), ('months', 'months')], default='year', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adopt',
            name='image',
            field=models.ImageField(default='defaultpet.jpeg', upload_to='Adopt_images'),
        ),
    ]
