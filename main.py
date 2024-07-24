import requests
import base64
import json
import spotipy
import detectLyricsLanguage
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from langdetect import detect


cid = ""
secret = ""
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri="http://localhost/"))

#número de músicas favoritadas
numMusicas = 2060
musicas = {}
i = 0
while i <= numMusicas:     
    results = sp.current_user_saved_tracks(limit=50, offset= i)
    for idx, item in enumerate(results['items']):
        track = item['track']
        musicas[i] = {
            "nome" : track['name'],
            "artista" : track['artists'][0]['name']
        }
        i += 1
    print(i)

for x in musicas:
    musica = musicas[x]
    nomeMusica = musica["nome"]
    nomeArtista = musica["artista"]
    lingua = detectLyricsLanguage.detectarLingua(nomeMusica=nomeMusica, nomeArtista=nomeArtista)
    print(nomeMusica)
    print(lingua)
    print("------------------------------------------")