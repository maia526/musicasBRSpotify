import requests
import base64
import json
import spotipy
import detectLyricsLanguage
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from langdetect import detect

# a API do genius tem uma limitação de 1000 músicas por dia
track_quantity = 10

#criando objeto spotipy com as autorizações
clientId = ""
secret = ""
scope = "user-library-read playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=clientId, client_secret=secret, redirect_uri="http://localhost/"))


def getSavedTracks(sp):
    #de 50 em 50, pegando todas as músicas favoritadas do usuário e guardando em 'musicas'
    i = 0
    while i < track_quantity:
        musicas = []
        results = sp.current_user_saved_tracks(limit=50, offset= i)
        for idx, item in enumerate(results['items']):
            track = item['track']
            musicas.append({
                "nome" : track['name'],
                "artista" : track['artists'][0]['name'],
                "uri": track['uri']
            })
            i += 1
        print(i)
    return musicas

def detectTracksLanguage():
    musicasBr = []
    musicasIndefinidas = []
    for musica in musicas:
        nomeMusica = musica["nome"]
        nomeArtista = musica["artista"]
        lingua = detectLyricsLanguage.detectarLingua(nomeMusica=nomeMusica, nomeArtista=nomeArtista)
        
        if lingua == "pt":
            musicasBr.append(musica)
        if lingua == "NotFound":
            musicasIndefinidas.append(musica)
        print(nomeMusica)
        print(lingua)
        print("------------------------------------------")
    return musicasBr, musicasIndefinidas

#número de músicas favoritadas
musicas = getSavedTracks(sp)
musicasBr, musicasIndefinidas = detectTracksLanguage()

#classificando manualmente as musicas br na lista de musicas indefinidas
print("\nResponda com s para sim ou n para n\n")
for musicaIndef in musicasIndefinidas:
    print(musicaIndef["nome"])
    isBR = input("\nÉ BR?").lower()

    if isBR == "s":
        musicasBr[len(musicasBr)] = musicaIndef

print("\n\nMUSICAS BR\n")
for musica in musicasBr:
    print(musica["nome"])
print("\n")

uris = []
for musica in musicasBr:
    uri = str(musica['uri'])
    uris.append(uri)

userId = "22bvkubaphqhby4irlz2oy5ty?si=a2d28945a57f40d2"
if (len(musicasBr) > 0):
    sp.user_playlist_add_tracks(tracks=uris, playlist_id="7z5I9aVchfBuLEM5Bvd18D", user=userId)