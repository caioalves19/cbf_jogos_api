from django.db import models


class Rodada(models.Model):
    numero = models.IntegerField(primary_key=True)


class Jogo(models.Model):
    numero = models.IntegerField(primary_key=True)
    rodada = models.ForeignKey(Rodada(), on_delete=models.DO_NOTHING)
    time_mandante = models.CharField(max_length=30)
    time_visitante = models.CharField(max_length=30)
    data = models.CharField(max_length=10, default="00/00/0000")
    hora = models.CharField(max_length=5, default="00:00")
    estadio = models.CharField(max_length=30, default="A definir")
    cidade = models.CharField(max_length=30, default="A definir")
    estado = models.CharField(max_length=2, default="--")

    def __str__(self):
        return f"{self.time_mandante} x {self.time_visitante}"
