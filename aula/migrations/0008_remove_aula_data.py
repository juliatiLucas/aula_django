# Generated by Django 3.0.7 on 2020-06-22 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0007_chamada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='data',
        ),
    ]
