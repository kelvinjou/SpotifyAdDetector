# SpotifyAdDetector
Helps detect Spotify ads and automatically skips them

Steps for setting up: 
1. Log into Spotify Developer Dashboard at https://developer.spotify.com/dashboard/
Use the email and password you signed up Spotify with. (i.e. mine ends with @gmail.com)

2. Once you are in the dashboard, select "Create New App", and fill in the required fields.

3. Copy your client ID and client secret and paste it as string values for `spotifyClientID`, and `spotifyClientSecret` variables in the `SpotifyAdDector.py` file.
Additionally, for the `spotifyUsername` variable, paste in the email you signed up with for Spotify(just like step 1 but without the pwd)

4. Go ahead and click `Edit Settings` in the app dashboard and fill in the uri: `http://localhost:8888/callback` under `redirect URIs` 
You don't have to fill the other fields, because they are only required by iOS, Android, etc.
Scroll to the bottom and click to the bottom and click "Save" or else it won't save(duh)
  Note: If you do change your `spotifyRedirectURI` value to something else(in the python file), you'll have to do it in the here as well.

5. run `pip install spotipy` and `pip install pynput` if you haven't already in your terminal/command prompt. (Pynput is probably already installed for you if        you're using an anaconda environment)

6. Go back into `SpotifyAdDetector.py` and comment/uncomment the lines of code depending what OS you are using.
  Note: Lines 35-46 are experimental for Mac users. If you do decide to uncomment those lines, comment out line 48.  
  
7. Lastly, run your code and it should work when an ad pops up on the PC/Mac Spotify App. 
Obvious stuff but: 
  - make sure you are running on the correct Python path that has the packages installed on.
  - MAC USERS ONLY: Go under `Security & Privacy` > `Privacy` > `Accessbility` and check "python" and "terminal" in the list view. 


![Screen Shot 2021-08-11 at 10 47 07 PM](https://user-images.githubusercontent.com/63611619/129144912-6eae2da1-b173-4fe7-b554-405fa491ee01.png)


Have fun! ;)
