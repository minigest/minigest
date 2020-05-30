from rest_framework import viewsets

from minigest.anagrafica.models import Utente
from rest.serializers import UtenteSerializer


class UtenteVS(viewsets.ModelViewSet):
    queryset = Utente.objects.all()
    serializer_class = UtenteSerializer
