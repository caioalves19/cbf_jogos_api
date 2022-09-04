from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cbf_api.views import JogoViewSet, ListaJogosPorRodada, ListaTodosJogos


router = routers.DefaultRouter()
router.register("jogos", viewset=JogoViewSet, basename="Jogos")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("jogos/all", ListaTodosJogos.as_view()),
    path("rodada/<int:num_rodada>", ListaJogosPorRodada.as_view()),
]
