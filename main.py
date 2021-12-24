import os
import requests
import time
from pynput.keyboard import Key, Controller
from refresh import Refresh
'''
curl -H "Authorization: Basic N2Y5YWUxZTk0NGVmNDFkNTg3YzhjZjA4YjRkODM1MGE6ODkxYmJiMDAwMzcxNDliNmExNDZhMDU0NjZkZDViMjg=" -d grant_type=authorization_code -d code=AQBYqA1RD0Pz8xS40oubOybB5LSTt1Aiv0j1viKRr17WMBUW9jVHvJJNMzdbwsHUQgpOTeg9sUl5h6UYrgTFXKjZa7mYeL36xM8dUz9IhQUVTurNVCP0UBqry1NsT33eiiULYxGoiRXByb80dzHeG4mEBRbW6dZzrdPEPEhS4yQUu6c_gkLE2Gj3LIdvxjTlvqV92p-LhfLGLKvKe9B5r-QC4jpldqw4U3jjpqWobg -d redirect_uri=https://google.com https://accounts.spotify.com/api/token
'''
start_time = time.time()
r = Refresh()

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = r.refresh()

class SpotifyApplicationManager:
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
        time.sleep(3.25)
    
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
        keyboard = Controller()
        keyboard.press(Key.space)

    def restartSpotify():
        SpotifyApplicationManager.closeSpotify()
        SpotifyApplicationManager.openSpotify()
        SpotifyApplicationManager.playSpotify()
        print("Ad skipped")

def get_current_track(access_token):
    global start_time
    print(time.time() - start_time)
    if (time.time() - start_time) > 3500:
        SPOTIFY_ACCESS_TOKEN = r.refresh()
        print("Refreshed token")

        # refreshing token expiration countdown
        start_time = time.time()
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL, 
        headers = {
            "Authorization" : f"Bearer {access_token}"
        }
    )
    resp_json = response.json()
    
    track_type = resp_json['currently_playing_type']
    # track_name = resp_json['item']['name']
    current_track_info = {
        # "song" : track_name,
        "type" : track_type
    }
    if track_type == "ad":
        SpotifyApplicationManager.restartSpotify()

def main():
    
    current_track_info = get_current_track(
        SPOTIFY_ACCESS_TOKEN
        )

if __name__ == '__main__':
    
    print("Initial token")
    
    while True:
        main()
        
        # print("entered")
        time.sleep(2)


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
