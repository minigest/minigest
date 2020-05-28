from django.urls import include, path

from rest_framework_nested import routers

from . import viewsets

""" DefaultRouter """
router = routers.DefaultRouter()


""" anagrafica """
router.register(r"utenti", viewsets.UtenteVS)
router.register(r"soggetti-fiscali", viewsets.SoggettoFiscaleVS)
router.register(r"persone-fisiche", viewsets.PersonaFisicaVS)
router.register(r"imprese", viewsets.ImpresaVS)


""" fisco """
router.register(r"fisco/regime-fiscale", viewsets.RegimeFiscaleVS)
router.register(r"fisco/interessi-legali", viewsets.InteressiLegaliVS)
router.register(r"fisco/tur", viewsets.TurVS)


""" imprese """
imprese = routers.NestedDefaultRouter(router, r"imprese", lookup="impresa")
imprese.register(r"negozi", viewsets.NegozioVS, basename="impresa-negozi")


""" negozio """
negozio = routers.NestedDefaultRouter(imprese, r"negozi", lookup="negozio")
negozio.register(r"orari", viewsets.OrarioVS, basename="negozio-orari")
negozio.register(
    r"orari-varianti", viewsets.OrarioVarianteVS, basename="negozio-orari-varianti"
)
negozio.register(r"sede", viewsets.NegozioSedeVS, basename="negozio-sede")
negozio.register(r"casse", viewsets.CassaVS, basename="negozio-casse")

""" negozio-cassa """
casse = routers.NestedDefaultRouter(negozio, r"casse", lookup="cassa")
casse.register(r"fondo", viewsets.FondoCassaVS, basename="casse-fondo")
casse.register(r"incassi", viewsets.IncassoVS, basename="incassi")

""" urlpatterns """
urlpatterns = [
    path("auth/", include("rest_framework.urls"), name="api-auth"),
    path("", include(router.urls)),
    path("", include(imprese.urls)),
    path("", include(negozio.urls)),
    path("", include(casse.urls)),
]
