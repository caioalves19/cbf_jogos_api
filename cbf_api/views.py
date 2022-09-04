import re
from rest_framework import viewsets, generics
from cbf_api.serializers import JogoSerializer
from cbf_api.models import Jogo
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaJogosPorRodada(generics.ListAPIView):
    def get_queryset(self):
        queryset = Jogo.objects.filter(rodada=self.kwargs["num_rodada"])
        return queryset

    serializer_class = JogoSerializer


class ListaTodosJogos(generics.ListAPIView):
    def get_queryset(self):
        queryset = Jogo.objects.all()
        return queryset

    serializer_class = JogoSerializer
