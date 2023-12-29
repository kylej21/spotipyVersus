import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import time
start_time = time.time()

def calcBetter(artistName1,artistName2):

    cid = ''
    secret = ''
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
        while data['next']:
            data = spotify.next(data)
            albums.extend(data['items'])

        for album in albums:
            albId=album["uri"].split(":")[2]
            data2=spotify.album_tracks(albId)
            for each in data2["items"]:
                songURI=each["id"]
                songData=spotify.track(songURI)
                popularity = songData["popularity"]
                duration = songData["duration_ms"]
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
        while data['next']:
            data = spotify.next(data)
            albums.extend(data['items'])

        for album in albums:
            albId=album["uri"].split(":")[2]
            data2=spotify.album_tracks(albId)
            for each in data2["items"]:
                songURI=each["id"]
                songData=spotify.track(songURI)
                popularity = songData["popularity"]
                duration = songData["duration_ms"]
                numArtist=len(songData["artists"])
                new_df= pd.DataFrame({"Popularity" : [popularity], "Duration" : [duration], "numArtists" :[numArtist]})
                artist2 = pd.concat([artist2, new_df], ignore_index=True)

    except:
        print("Artist not found. Rerun program to try again")
        exit()
    outputString=""
    outputString+= "Time to decide who is the better artist between " + artistName1 + " and " + artistName2 + "."
    outputString+= "\n"
    outputString+="Success factor: " + artistName1 + " - " + str(round(artist1["Popularity"].mean(),2)) + "\t " + artistName2 + " - " + str(round(artist2["Popularity"].mean(),2))
    outputString+= "\n"
    outputString+="Song length: " + artistName1 + " - " + str(int(artist1["Duration"].mean()//1000//60)) + " minutes and " + str(int(artist1["Duration"].mean()//1000%60)) + " seconds " + "\t " + artistName2 + " - " + str(int(artist2["Duration"].mean()//1000//60)) + " minutes and " + str(int(artist2["Duration"].mean()//1000%60)) + " seconds"
    outputString+="\n"
    outputString+="Collab factor: " + artistName1 + " - " + str(round(artist1["numArtists"].mean(),2)) + "\t " + artistName2 + " - " + str(round(artist2["numArtists"].mean(),2))
    print(outputString)
    finWinner=0
    finWinner += (artist1["Popularity"].mean()-artist2["Popularity"].mean())*10
    finWinner += (int(artist1["Duration"].mean())-int(artist2["Duration"].mean()))//60000
    finWinner += (artist2["numArtists"].mean() - artist1["numArtists"].mean())*3
    if finWinner ==0 :
        print("Wow! It's a tie. Both artists are perfectly balanced")
    elif finWinner > 0:
        print(artistName1 + " wins!")
    else:
        print(artistName2 + " wins!")
    
    
   

print("What artist do you want to search for?")
artistName1=input()
print("Who is the second artist you want to compare")
artistName2=input()
print("Loading many API requests, please wait...")
calcBetter(artistName1,artistName2)
print("Process finished --- %s seconds ---" % round((time.time() - start_time),3))