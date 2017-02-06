from django import forms

class ArtistSearchForm(forms.Form):
    artist_name = forms.CharField(label='Artist Name', max_length=100)
