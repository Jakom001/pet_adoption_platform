# Generated by Django 5.0.3 on 2024-03-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptpet', '0003_adopt_month_year_alter_adopt_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopt',
            old_name='category',
            new_name='species',
        ),
        migrations.AddField(
            model_name='adopt',
            name='breed',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='adopt',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adopt',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]