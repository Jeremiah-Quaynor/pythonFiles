import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import time


# clientId = "311e47461d1944a6ba6977c4967c537e"
# clientSecret = "697c5c540cac4dfe8f0868d9a6745189"
# redirectURL = "https://www.google.com/"

username = "wui5sa0fm7e298dkak11vlhxx"
playlistID = f"spotify:user:{username}:playlist:014OLvGgM0WeI9y40U6FOu" #user playlist format
# playlistID = f"spotify:artist:2WX2uTcsvV5OnS0inACecP" #artist playlist format

device = ""
scope = 'user-library-read, user-read-playback-state, user-modify-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

devices = sp.devices()
print(json.dumps(devices, indent=4))
device1 = devices['devices'][0]['id']
device2 = devices['devices'][1]['id']
print(device1, device2)
# counter = 0

# sp.start_playback(context_uri=playlistID)
# cp = sp.currently_playing()
# print("first",cp['progress_ms'])
# for i in range(1,10):
#     time.sleep(1)
#     counter += 1
#     print(counter)

# cp = sp.currently_playing()
# print("second",cp['progress_ms'])
# sp.transfer_playback(device_id=devices["devices"][0]["id"],force_play=True)
sp.start_playback(device_id=device2, context_uri=playlistID)
# time.sleep(35)
# sp.pause_playback(device_id=device2)
# time.sleep(35)
# sp.next_track(device_id=device2)
# print("final",counter)



