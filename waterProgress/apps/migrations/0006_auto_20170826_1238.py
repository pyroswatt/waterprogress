# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_moteur_voiture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('produits', models.ManyToManyField(through='blog.Offre', to='blog.Produit')),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Vendeur'),
        ),
    ]