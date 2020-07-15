# Generated by Django 3.0.8 on 2020-07-15 08:44

import django.core.validators
from django.db import migrations, models
import minigest.common.models.fields.uppercase


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InteressiLegali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('percentuale', models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Interessi legali',
                'verbose_name_plural': 'Interessi legali',
                'ordering': ('-data',),
            },
        ),
        migrations.CreateModel(
            name='RegimeFiscale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', minigest.common.models.fields.uppercase.UpperCaseField(max_length=5, unique=True)),
                ('descrizione', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'regimi fiscali',
            },
        ),
        migrations.CreateModel(
            name='TassoUfficialeRiferimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('percentuale', models.DecimalField(decimal_places=2, max_digits=19, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
            options={
                'verbose_name': 'Tasso Ufficiale di Riferimento',
                'verbose_name_plural': 'Tassi ufficiali di Riferimento',
                'ordering': ('-data',),
            },
        ),
    ]