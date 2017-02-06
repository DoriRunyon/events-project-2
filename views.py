from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os, spotipy
from forms import ArtistSearchForm
import json
from django.http import HttpResponseRedirect
from pprint import pprint

songkick_api_key = os.environ['SONGKICK_API_KEY']
spotify_consumer_key = os.environ['SPOTIFY_CONSUMER_KEY']
spotify_consumer_secret = os.environ['SPOTIFY_CONSUMER_SECRET']
google_maps_api_key = os.environ['GOOGLE_MAPS_API_KEY']

spotify = spotipy.Spotify()

def index(request):
    return render(request, 'events/index.html')

def search_no_login(request):

    form = ArtistSearchForm(request.GET)
    related_artist_list = []

    if form.data:
        a = form.data['artist_name']
        related = get_related_artists(a)
        for artist in related:
            name = artist['name']
            related_artist_list.append(name)
        return render(request, 'events/search_no_login.html', {'artist': a, 'related_artist_list': related_artist_list})

    return render(request, 'events/search_no_login.html')

#@login_required - eventually will put this here because this is a login only page
def logged_in_dashboard(request):
    return render(request, 'events/logged_in_dashboard.html')

def get_artist_spotify_uri(spotify, artist):
    """Get artist spotify URI."""

    artist_search = spotify.search(artist, limit=1, offset=0, type='artist')
    if artist_search['artists']['items'] == []:
        return None
    else:
        artist_uri = artist_search['artists']['items'][0]['uri'].lstrip("spotify:artist:")

    return artist_uri

def get_related_artists(artist):
    """Get Spotify list of related artists for an artist."""

    artist_spotify_id = get_artist_spotify_uri(spotify, artist)
    related_artists = spotify.artist_related_artists(artist_spotify_id)
    related_artists = related_artists['artists']

    return related_artists