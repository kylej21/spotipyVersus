import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import sys

def calcBetter(artistName1,artistName2):

    cid = 'b1a844a5bc41486b8a7704fa54391a89'
    secret = '1d3f9abd9b5f41a4a7c268a1f0e106fc'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    artist1 = pd.DataFrame({
        "Duration" : [],
        "Popularity" : [],
        "numArtists": []
    })
    artist2 = pd.DataFrame({
        "Duration" : [],
        "Popularity" : [],
        "numArtists": []
    })
    try:
        result=spotify.search(q=f"{artistName1}",type="artist",limit=1)
        uri=result["artists"]["items"][0]["uri"]
        data = spotify.artist_albums(uri, album_type='album')
        albums = data['items']
        songs=[]
        while data['next']:
            data = spotify.next(data)
            albums.extend(data['items'])

        for album in albums:
            albId=album["uri"].split(":")[2]
            data2=spotify.album_tracks(albId)
            for each in data2["items"]:
                #songs[each['duration_ms']]=each["name"]
                songURI=each["id"]
                songData=spotify.track(songURI)
                popularity = songData["popularity"]
                duration = songData["duration_ms"]
                name=songData['name']
                numArtist=len(songData["artists"])
                new_df= pd.DataFrame({"Popularity" : [popularity], "Duration" : [duration], "numArtists" :[numArtist]})
                artist1 = pd.concat([artist1, new_df], ignore_index=True)

    except:
        print("Artist not found. Rerun program to try again")
        exit()
    try:
        result=spotify.search(q=f"{artistName2}",type="artist",limit=1)
        uri=result["artists"]["items"][0]["uri"]
        data = spotify.artist_albums(uri, album_type='album')
        albums = data['items']
        songs=[]
        while data['next']:
            data = spotify.next(data)
            albums.extend(data['items'])

        for album in albums:
            albId=album["uri"].split(":")[2]
            data2=spotify.album_tracks(albId)
            for each in data2["items"]:
                #songs[each['duration_ms']]=each["name"]
                songURI=each["id"]
                songData=spotify.track(songURI)
                popularity = songData["popularity"]
                duration = songData["duration_ms"]
                name=songData['name']
                numArtist=len(songData["artists"])
                new_df= pd.DataFrame({"Popularity" : [popularity], "Duration" : [duration], "numArtists" :[numArtist]})
                artist2 = pd.concat([artist2, new_df], ignore_index=True)

    except:
        print("Artist not found. Rerun program to try again")
        exit()
    outputString=""
    outputString+= "Time to decide who is the better artist between " + artistName1 + " and " + artistName2 + "."
    outputString+= "\n"
    outputString+="Success factor: " + artistName1 + " - " + str(artist1["Popularity"].mean()) + "\t " + artistName2 + " - " + str(artist2["Popularity"].mean())
    outputString+= "\n"
    outputString+="Song length factor: " + artistName1 + " - " + str(artist1["Duration"].mean()) + "\t " + artistName2 + " - " + str(artist2["Duration"].mean())
    outputString+="\n"
    outputString+="Collab factor: " + artistName1 + " - " + str(artist1["numArtists"].mean()) + "\t " + artistName2 + " - " + str(artist2["numArtists"].mean())
    return(outputString)

print("What artist do you want to search for?")
artistName1=input()
print("Who is the second artist you want to compare")
artistName2=input()
print("Loading many API requests, please wait...")
print(calcBetter(artistName1,artistName2))
