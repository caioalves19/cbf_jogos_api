import imp
from django.contrib import admin
from cbf_api.models import Jogo, Rodada


class Jogos(admin.ModelAdmin):
    list_display = (
        "numero",
        "time_mandante",
        "time_visitante",
        "data",
        "hora",
        "estadio",
        "cidade",
        "estado",
    )
    list_display_links = ("numero", "time_mandante", "time_visitante")


admin.site.register(Jogo, Jogos)


class Rodadas(admin.ModelAdmin):
    list_display = ["numero"]
    list_display_links = ["numero"]


admin.site.register(Rodada, Rodadas)
