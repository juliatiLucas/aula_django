# Generated by Django 3.0.7 on 2020-06-20 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('aula', '0006_tarefa_prazo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Aluno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.Aula')),
            ],
        ),
    ]
