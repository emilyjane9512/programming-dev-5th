# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 06:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('captured_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon.User'),
        ),
        migrations.AddField(
            model_name='capture',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon.User'),
        ),
        migrations.AddField(
            model_name='capture',
            name='pokemon',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pokemon.Pokemon'),
        ),
    ]
