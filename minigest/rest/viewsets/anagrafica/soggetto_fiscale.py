from rest_framework import viewsets

from minigest.anagrafica.models import SoggettoFiscale as sf
from minigest.rest.serializers import SoggettoFiscalePolymorphicSerializer


class SoggettoFiscale(viewsets.ModelViewSet):
    queryset = sf.objects.all()
    serializer_class = SoggettoFiscalePolymorphicSerializer