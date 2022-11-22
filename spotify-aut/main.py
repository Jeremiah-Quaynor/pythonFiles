import requests
import base64,json
from secrets import *


# curl -x "POST" -H "Authorization: Basic khhk..jhgjgWY0MzE=" -d grant_type=client_credentials https://accounts.spotify.com/api/token

authURL = "https://accounts.spotify.com/api/token"
authHeader = {}
authData= {}

# base64 encode client ID and Client Secret

def getAccessToken(clientID, ClientSecret):
    message = f"{clientID}:{ClientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    # print(base64_message)
    authHeader['Authorization'] = "Basic " + base64_message
    authData['grant_type'] = "client_credentials"
    res = requests.post(authURL, headers= authHeader, data=authData)
    responseObject = res.json()
    # print(json.dumps(responseObject, indent=2))
    accessToken = responseObject['access_token']
    return accessToken


def getPlaylistTracks(token, playlistid):
    playlistEndPoint = f"https://api.spotify.com/v1/playlists/{playlistid}"
    
    getHeader = {
        'Authorization': "Bearer "+ token
    }
    res = requests.get(playlistEndPoint, headers=getHeader)

    playlistObject = res.json()
    
    return playlistObject

# API requests
token = getAccessToken(clientId, clientSecret)
playlistID = "5T30b2ycCSKIQdVVH8VaK5?si=304d55cc7a2641d6"
tracklist = getPlaylistTracks(token,playlistID)
# print(json.dumps(tracklist, indent=2))

with open('trackList.json', 'w') as f:
    json.dump(tracklist,f)


for t in tracklist['tracks']['items']:
    songName = t['track']['name']
    print(songName)