# Generated by Django 3.0.7 on 2020-06-23 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0011_auto_20200622_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datachamada',
            name='data',
            field=models.DateField(),
        ),
    ]
