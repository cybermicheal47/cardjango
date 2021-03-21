# Generated by Django 3.0.8 on 2021-03-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='doors',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cars',
            name='fuel_type',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cars',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
