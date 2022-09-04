# Generated by Django 4.1 on 2022-09-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbf_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JogosPorRodada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='jogo',
            old_name='numero_jogo',
            new_name='numero',
        ),
        migrations.AddField(
            model_name='jogo',
            name='data',
            field=models.CharField(default='00/00/0000', max_length=10),
        ),
        migrations.AddField(
            model_name='jogo',
            name='hora',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='estado',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='time_mandante',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='time_visitante',
            field=models.CharField(max_length=30),
        ),
    ]