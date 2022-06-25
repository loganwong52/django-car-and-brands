# Generated by Django 2.1.3 on 2022-06-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_and_brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='car',
            name='number_of_seats',
            field=models.IntegerField(default=4),
        ),
    ]
