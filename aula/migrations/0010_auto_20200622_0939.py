# Generated by Django 3.0.7 on 2020-06-22 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0009_auto_20200622_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamada',
            name='data_chamada',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='aula.DataChamada'),
        ),
    ]
