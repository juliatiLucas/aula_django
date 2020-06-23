# Generated by Django 3.0.7 on 2020-06-22 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0008_remove_aula_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataChamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chamada',
            name='data',
        ),
        migrations.AddField(
            model_name='chamada',
            name='data_chamada',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aula.DataChamada'),
        ),
    ]
