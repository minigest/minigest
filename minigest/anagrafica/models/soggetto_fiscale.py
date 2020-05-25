from django.core.validators import MinLengthValidator
from django.db import models

from polymorphic.models import PolymorphicModel

from minigest.common.models.fields import UpperCaseField
from ..helpers.impresa import pagamenti


class SoggettoFiscale(PolymorphicModel):
    """
    Il codice destinatario per le fatture elettroniche.
    Per le PA sono 6 cifre, per i privati 7
    - Se il soggetto fiscale non ha un codice destinatario
      riepire il campo con il segno 0
    - Se il soggetto fiscale risiede al di fuori dell'Italia,
      il campo va riempito con il segno X
    """

    codice_destinatario = UpperCaseField(
        blank=False,
        null=False,
        default="0000000",
        max_length=7,
        validators=[MinLengthValidator(6)],
    )

    email = models.EmailField(
        blank=True, null=True, max_length=256, validators=[MinLengthValidator(7)]
    )

    """ Altri campi comuni a tutti i soggetti fiscali """

    telefono = models.CharField(
        blank=True, null=True, max_length=12, validators=[MinLengthValidator(5)]
    )

    fax = models.CharField(
        blank=True, null=True, max_length=12, validators=[MinLengthValidator(5)]
    )

    rappresentante_fiscale = models.OneToOneField(
        to="self", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )

    def pagamenti(self, dal=None, al=None):
        return pagamenti(self, dal, al)

    class Meta:
        verbose_name_plural = "soggetti fiscali"
