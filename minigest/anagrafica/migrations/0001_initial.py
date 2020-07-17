# Generated by Django 3.0.8 on 2020-07-17 15:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import minigest.common.models.fields.uppercase


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('fisco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoggettoFiscale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, help_text='titolo onorifico', max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('nome', models.CharField(max_length=60)),
                ('cognome', models.CharField(max_length=60)),
                ('codice_fiscale', minigest.common.models.fields.uppercase.UpperCaseField(max_length=16, validators=[django.core.validators.MinLengthValidator(11)])),
                ('codice_destinatario', minigest.common.models.fields.uppercase.UpperCaseField(default='0000000', max_length=7, validators=[django.core.validators.MinLengthValidator(6)])),
                ('email', models.EmailField(blank=True, max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(7)])),
                ('telefono', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('fax', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(5)])),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_anagrafica.soggettofiscale_set+', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'soggetti fiscali',
            },
        ),
        migrations.CreateModel(
            name='DomicilioStabileOrganizzazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indirizzo', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(1)])),
                ('numero_civico', models.CharField(blank=True, max_length=10, null=True)),
                ('cap', models.CharField(default='00000', help_text='per paesi extra EU inserire 00000', max_length=5, validators=[django.core.validators.MinLengthValidator(5)])),
                ('comune', models.CharField(max_length=60)),
                ('provincia', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, help_text='es: MI - da valorizzare solo se nazione è uguale a IT (Italia)', max_length=2, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('nazione', minigest.common.models.fields.uppercase.UpperCaseField(help_text='es: IT', max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('soggetto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stabile_organizzazione', to='anagrafica.SoggettoFiscale')),
            ],
            options={
                'verbose_name_plural': 'Stabile organizzazione',
            },
        ),
        migrations.CreateModel(
            name='DomicilioFiscale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indirizzo', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(1)])),
                ('numero_civico', models.CharField(blank=True, max_length=10, null=True)),
                ('cap', models.CharField(default='00000', help_text='per paesi extra EU inserire 00000', max_length=5, validators=[django.core.validators.MinLengthValidator(5)])),
                ('comune', models.CharField(max_length=60)),
                ('provincia', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, help_text='es: MI - da valorizzare solo se nazione è uguale a IT (Italia)', max_length=2, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('nazione', minigest.common.models.fields.uppercase.UpperCaseField(help_text='es: IT', max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('soggetto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='domicilio_fiscale', to='anagrafica.SoggettoFiscale')),
            ],
            options={
                'verbose_name_plural': 'Domicilio fiscale',
            },
        ),
        migrations.CreateModel(
            name='PersonaFisica',
            fields=[
                ('soggettofiscale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='anagrafica.SoggettoFiscale')),
                ('utente', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dettagli_fiscali', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Persone fisiche',
            },
            bases=('anagrafica.soggettofiscale',),
        ),
        migrations.CreateModel(
            name='Impresa',
            fields=[
                ('soggettofiscale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='anagrafica.SoggettoFiscale')),
                ('denominazione', models.CharField(help_text="la denominazione dell'impresa o il nome e cognome", max_length=80)),
                ('codice_eori', models.CharField(blank=True, default=None, help_text='Economic Operator Registration and Identification', max_length=17, null=True, validators=[django.core.validators.MinLengthValidator(13)])),
                ('id_fiscale_iva_paese', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, default=None, help_text='es: IT', max_length=2, null=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='codice paese partita IVA')),
                ('id_fiscale_iva_codice', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, default=None, help_text='per paesi extra EU inserire 99999999999', max_length=28, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='codice partita IVA')),
                ('albo_professionale', models.CharField(blank=True, default=None, help_text="nome dell'albo professionale", max_length=60, null=True)),
                ('albo_provincia', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, default=None, help_text='es: MI', max_length=2, null=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Provincia Albo')),
                ('albo_numero_iscrizione', models.CharField(blank=True, default=None, help_text="numero di iscrizione all'albo professionale", max_length=60, null=True, verbose_name='Numero iscrizione Albo')),
                ('albo_data_iscrizione', models.DateField(blank=True, default=None, help_text="data di iscrizione all'albo professionale", null=True, verbose_name="Data di iscrizione all'Albo")),
                ('rea_ufficio', minigest.common.models.fields.uppercase.UpperCaseField(blank=True, default=None, help_text="provincia dell'Ufficio REA, es: MI", max_length=2, null=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Ufficio REA')),
                ('rea_numero', models.CharField(blank=True, default=None, help_text='numero di iscrizione al registro delle imprese', max_length=60, null=True, verbose_name='Numero REA')),
                ('capitale_sociale', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='nei casi di società di capitali', max_digits=15, null=True)),
                ('socio_unico', models.CharField(blank=True, choices=[(None, None), ('SU', 'socio unico'), ('SM', 'più soci')], default=None, help_text='nei casi di società per azioni a responsabilità limitata', max_length=2, null=True)),
                ('stato_liquidazione', models.CharField(blank=True, choices=[(None, None), ('LS', 'in liquidazione'), ('LN', 'non in liquidazione')], default=None, help_text='indica se la società si trova in stato di liquidazione o no', max_length=2, null=True)),
                ('riferimento_amministrazione', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='codice identificativo del cedente ai fini amministrativo-contabili', max_digits=20, null=True)),
                ('pec', models.EmailField(blank=True, max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(7)])),
                ('regime_fiscale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='imprese', to='fisco.RegimeFiscale', to_field='codice')),
                ('utenti', models.ManyToManyField(blank=True, related_name='imprese', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Imprese',
            },
            bases=('anagrafica.soggettofiscale',),
        ),
    ]
