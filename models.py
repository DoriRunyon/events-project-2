from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    #need to fix password field
    password = models.CharField(max_length=50)

class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_songkick_id = models.CharField(max_length=100)
    artist_spotify_id = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=50)
    artist_img = models.CharField(max_length=100)
    artist_popularity = models.FloatField(max_length=100)


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_songkick_id = models.CharField(max_length=100)
    artist_id = models.ForeignKey(Artist)
    event_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lat = models.FloatField(max_length=100)
    lng = models.FloatField(max_length=100)
    event_songkick_link = models.CharField(max_length=200)
    datetime = models.DateTimeField(max_length=100)

class UserSavedEvent(models.Model):
    user_id = models.ForeignKey(User)
    event_id = models.ForeignKey(Event)

