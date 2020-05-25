import itertools
from operator import itemgetter

from pydash import flatten


def riepilogo_reparti_queryset(self):
    chiusure = self.all()

    # crea una lista di tutti i reparti
    reparti = list()

    for chiusura in chiusure:
        reparti.append(chiusura.dettagli)

    # aggiusta la lista dei reparti
    reparti = flatten(reparti)

    # ordina i reparti per aliquota iva
    reparti = sorted(reparti, key=itemgetter("iva_aliquota"))

    # raggruppa i reparti per aliquota iva
    reparti = itertools.groupby(reparti, key=itemgetter("iva_aliquota"))

    # Aggrega i reparti per aliquota iva
    riepilogo = list()

    for aliquota, reparto in reparti:
        dettagli = {
            "iva_aliquota": aliquota,
            "totale": 0,
            "imposta": 0,
            "imponibile": 0,
            "totale_lordo": 0,
            "non_riscosso": 0,
            "annulli": 0,
            "resi": 0,
        }

        # somma i valori del reparto
        for v in reparto:
            dettagli["totale"] += v["totale"]
            dettagli["imposta"] += v["imposta"]
            dettagli["imponibile"] += v["imponibile"]
            dettagli["totale_lordo"] += v["totale_lordo"]
            dettagli["non_riscosso"] += v["non_riscosso"]
            dettagli["annulli"] += v["annulli"]
            dettagli["resi"] += v["resi"]

        # aggiunge il reparto alla lista dei reparti aggregati
        riepilogo.append(dettagli)

    # ritora la lista dei reparti aggregati
    return riepilogo
