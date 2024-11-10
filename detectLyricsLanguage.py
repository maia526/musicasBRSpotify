import requests
from lyricsgenius import Genius
from langdetect import detect

def detectarLingua(nomeMusica, nomeArtista):
    token = "8aGtIIz8kQbHXnX-AwVlgAv0CK7QbfLjICEm3OjpPOzinOL6OmRNM6kl-qLn65Ww"
    genius = Genius(token)
    song = genius.search_song(title=nomeMusica, artist=nomeArtista)
    if (song == None):
        return "NotFound"
    return detect(song.lyrics)
