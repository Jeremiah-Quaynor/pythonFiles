import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import json
import time
from datetime import datetime
import random
from configurations import credentials,playlist


DAY = 600 #86400 #day in seconds
# daily constraints
MIN_DAY_PLAY_DURATION = 130  #30856 # 8hr 34m 16s
MAX_DAY_PLAY_DURATION = 250 #72013 # 20hr 13s
# Breaks
MAX_BREAK_DURATION = 120 #14400 # 4hr spread over 3 times a day

PLAY_TIME_DURATION = 30 # 30s

DAILY_DURATIONS = [MIN_DAY_PLAY_DURATION,MAX_DAY_PLAY_DURATION]

#boolean values
random_states = [True,False]

start = True



REDIRECT_URL = "https://www.google.com/"
SCOPE = 'user-library-read, user-read-playback-state, user-modify-playback-state'

OAUTH = SpotifyOAuth(scope=SCOPE, client_id = credentials["CLIENT_ID"], client_secret = credentials["CLIENT_SECRET"],redirect_uri=REDIRECT_URL)
sp = spotipy.Spotify(auth_manager= OAUTH)

# getting device ID
devices = sp.devices()
DEVICE_ID = devices['devices'][0]['id']



# ----------- time functions ----------------------------
def read_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def generate(start,end):
    return random.randint(start,end)

def random_daily_duration():
    daily_playtime = generate(0,len(DAILY_DURATIONS)-1) # from 1 to 2
    return DAILY_DURATIONS[daily_playtime]

def get_current_time(): ##return current time in seconds
    seconds = datetime.today()
    return seconds.timestamp()




# picking a day
generated_daily_duration = random_daily_duration()
print("generated play day duration",read_time(generated_daily_duration))

start_time = get_current_time()
print("start time", read_time(start_time))

end_time = start_time + generated_daily_duration
print("end time", read_time(end_time))

# working with break
max_break_time = 60 #i7200 # 2 hours
break_time_count =  3 #3 times a day
break_time_counter = 0


def break_and_sleep():
    random_break = generate(40,max_break_time)# 40s and 60s
    random_break_start = get_current_time()
    random_break_end = random_break_start + random_break #get time from app start to a random end
    sp.pause_playback(device_id=DEVICE_ID)
    # stop the song
    print("stop song", read_time(random_break_start))
    print("random sleep time",random_break)
    time.sleep(random_break)
    if get_current_time() == random_break_end:
        # start song
        print("resume song",read_time(get_current_time))
        sp.start_playback(device_id=DEVICE_ID)


def check_song_progress(cp):
    print("checking progress...")
    global random_states #the list with True of False in it
    if cp['progress_ms'] >= 1000 and cp['progress_ms'] <= 15000: #check progress between 1s and 15s
        state = generate(0,1)
        if random_states[state]:
            print("Play for 30s")
            time.sleep(30)
            sp.next_track(device_id=DEVICE_ID)
            print("skipping song")




def play_list_uri(ids_list):
    all_playlist = []
    for ids in ids_list:
        all_playlist.append(f"spotify:user:{credentials['USERNAME']}:playlist:{ids}")
    print(all_playlist)
    return all_playlist

def artist_list_uri(ids_list):
    all_artist = []
    for ids in ids_list:
        all_artist.append(f"spotify:artist:{ids}")
    print(all_artist)
    return all_artist

def convert_playlist(playlist_uri_list,artist_uri_list):
    a = playlist_uri_list
    a.extend(artist_uri_list)
    return a
    
new_playlist = convert_playlist(play_list_uri(playlist['PLAYLIST_IDS']),artist_list_uri(playlist['ARTIST']))
# print(type(new_playlist), new_playlist)
# time.sleep(10)

try:

    while start:
        play_list = generate(0,len(new_playlist)-1)
        # for a day, play 8hr... or 20hr ...
        current_time = get_current_time()
        if current_time >= start_time and current_time <= end_time:
            # do something today 
            print("do something today", read_time(get_current_time()))
            sp.start_playback(device_id=DEVICE_ID,context_uri=new_playlist[play_list])
            
            # check song progress    
            cp = sp.currently_playing() #find the song playings duration 
            check_song_progress(cp)

            # capture time to sleep
            # if break_time_counter < break_time_count:
            #     break_and_sleep()
            # break_time_counter += 1
            
        else:
            #sleep for the remaing day 
            # max play duration reached
            print("max play duration reached",get_current_time())
            sp.pause_playback(device_id=DEVICE_ID)
            remain_time_left_for_today = abs(DAY - end_time)
            time.sleep(remain_time_left_for_today)



except KeyboardInterrupt:
    print(read_time(start_time))























# sjhvdsjhbsdjhs-----------------------------------------------------------------------------



