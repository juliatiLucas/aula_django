# Generated by Django 3.0.7 on 2020-06-22 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0010_auto_20200622_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamada',
            name='aula',
        ),
        migrations.AddField(
            model_name='chamada',
            name='presente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datachamada',
            name='aula',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='aula.Aula'),
        ),
        migrations.AlterField(
            model_name='chamada',
            name='data_chamada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.DataChamada'),
        ),
    ]
