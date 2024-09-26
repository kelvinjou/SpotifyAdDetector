# from secrets import refresh_token, base_64
import requests
import json

refresh_token = "TOKEN"
base_64 = "N2Y5YWUxZTk0NGVmNDFkNTg3YzhjZjA4YjRkODM1MGE6ODkxYmJiMDAwMzcxNDliNmExNDZhMDU0NjZkZDViMjg="
class Refresh:
    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64 = base_64

    def refresh(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query, 
        data = {
            "grant_type" : "refresh_token", 
            "refresh_token" : refresh_token
        }, 
        headers = { "Authorization" : "Basic " + base_64 }
        )

        resp = response.json()
        new_token = resp['access_token']
        return new_token
        # return response.json()

a = Refresh()
a.refresh()
