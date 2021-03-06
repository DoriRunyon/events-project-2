# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_songkick_id', models.CharField(max_length=100)),
                ('artist_spotify_id', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=50)),
                ('artist_img', models.CharField(max_length=100)),
                ('artist_popularity', models.FloatField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_songkick_id', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('lat', models.FloatField(max_length=100)),
                ('lng', models.FloatField(max_length=100)),
                ('event_songkick_link', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField(max_length=100)),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserSavedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.User')),
            ],
        ),
    ]
