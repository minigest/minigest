# Generated by Django 3.0.7 on 2020-06-10 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0004_auto_20200528_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelazioneAziendale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utente', to='anagrafica.Impresa')),
                ('utente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impresa', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Relazioni Aziendali',
            },
        ),
    ]
