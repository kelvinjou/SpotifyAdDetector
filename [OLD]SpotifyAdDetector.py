# SpotifyAdDetector
# by @kelvinjou (modified from @Sakdev for mac compat)

import os
import time
import spotipy as sp
import spotipy.util as util
from pynput.keyboard import Key, Controller

keyboard = Controller()


def closeSpotify():
    '''For windows'''
    # os.system("taskkill /f /im spotify.exe")

    '''For mac'''
    os.system('killall -KILL Spotify')

    time.sleep(0.25)


def openSpotify():
    '''For windows'''
    # os.system('spotify.exe')

    '''For mac'''
    os.system('open /Applications/Spotify.app')
    time.sleep(0.25)


def playSpotify():
    time.sleep(1.25)
    
    '''for mac function keys'''
    # keyboard.press(Key.media_play_pause)
    # keyboard.release(Key.media_play_pause)
    # keyboard.press(Key.media_next)
    # keyboard.release(Key.media_next)
    # time.sleep(2.0)
    # keyboard.press(Key.alt_l)
    # keyboard.press(Key.tab)
    # keyboard.release(Key.alt_l)
    # keyboard.release(Key.tab)
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    keyboard.press(Key.space)



def restartSpotify():
    closeSpotify()
    openSpotify()
    playSpotify()
    print("Ad skipped")


spotifyUsername = "YOUR_SPOTIFY_EMAIL"
spotifyClientID = "CLIENT_ID"
spotifyClientSecret = "CLIENT_SECRET"
spotifyAccessScope = "user-read-currently-playing user-modify-playback-state"
spotifyRedirectURI = "http://localhost:8888/callback"

def setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
    token = util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
    return sp.Spotify(auth=token)


def main():
    global spotifyObject

    try:
        trackInfo = spotifyObject.current_user_playing_track()
        
        
    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except ConnectionError:
        print("Token Expired")
        spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,
                                           spotifyRedirectURI)
        trackInfo = spotifyObject.current_user_playing_track()
     
        

    try:
        
        if trackInfo['currently_playing_type'] == 'ad':
            
            restartSpotify()
    except TypeError:
        pass

    '''
    use print(trackInfo) here to get live data about the currently playing track
    i.e. print((trackInfo['item']["duration_ms"]))
    '''
    

spotifyObject = setupSpotifyObject(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret,
                                   spotifyRedirectURI)

while (True):
    main()
