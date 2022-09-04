# Generated by Django 4.1 on 2022-08-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('time_mandante', models.CharField(max_length=15)),
                ('time_visitante', models.CharField(max_length=15)),
                ('numero_jogo', models.IntegerField(primary_key=True, serialize=False)),
                ('estadio', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=15)),
            ],
        ),
    ]