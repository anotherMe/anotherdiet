# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('parte_edibile', models.FloatField()),
                ('energia_Kcal', models.FloatField()),
                ('energia_KJ', models.FloatField()),
                ('acqua', models.FloatField()),
                ('proteine_tot', models.FloatField()),
                ('proteine_anim', models.FloatField()),
                ('proteine_veg', models.FloatField()),
                ('glucidi_tot', models.FloatField()),
                ('amido', models.FloatField()),
                ('glucidi_solub', models.FloatField()),
                ('lipidi_tot', models.FloatField()),
                ('saturi', models.FloatField()),
                ('monoins', models.FloatField()),
                ('polins', models.FloatField()),
                ('acido_oleico', models.FloatField()),
                ('acido_linoleico', models.FloatField()),
                ('acido_linolenico', models.FloatField()),
                ('altri_polins', models.FloatField()),
                ('colesterolo', models.FloatField()),
                ('fibre', models.FloatField()),
                ('alcool', models.FloatField()),
                ('ferro', models.FloatField()),
                ('calcio', models.FloatField()),
                ('sodio', models.FloatField()),
                ('potassio', models.FloatField()),
                ('fosforo', models.FloatField()),
                ('zinco', models.FloatField()),
                ('vitamina_B1', models.FloatField()),
                ('vitamina_B2', models.FloatField()),
                ('vitamina_B3', models.FloatField()),
                ('vitamina_C', models.FloatField()),
                ('vitamina_B6', models.FloatField()),
                ('acido_folico', models.FloatField()),
                ('retinolo', models.FloatField()),
                ('beta_carotene', models.FloatField()),
                ('vitamina_E', models.FloatField()),
                ('vitamina_D', models.FloatField()),
            ],
        ),
    ]
