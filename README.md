# spotipyVersus
Repo for implementing spotify's python API - Spotipy. Versus contest between two artists to determine which is the better or 
more accomplished artist.

# Required Dependencies:
- Python
- Pandas

# Setup:

You will need a Spotify Client ID and secret to run this software. In order to get this information follow these steps:
1- go to https://developer.spotify.com/ and create your own spotify app. It does not matter what you name it
2- After making your app click settings and collect your Client ID and Client Secret.
3- Fill in the corresponding lines on Main.py with your Client ID and secret.
4- when in the correct directory enter ```Python3 main.py``` 
5- Respond to prompts and wait for it to analyze.


Decision Making Process:

The idea behind the formula to determine who wins is three main factors provided by the Spotipy API: Success, Song Length, and Features.
Success is weighed the most heavily in the formula because an Artists success typically is representative of music that is widely enjoyed.
Song Length is weighed the second heaviest. The idea behind using song length is that it is more significant if you have a 3 minute 
perfect song than a 30 second perfect song. Finally, the number of feature artists that typically show up on a song is used against the 
artist. The idea behind this is that an artist who achieves a perfect song by himself is more accomplished than one who does it with a 
duo. Since songs with multiple artists reach a larger audience this helps balance out the formula against artists who have songs with 
a lot of features. 
