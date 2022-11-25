import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import time
import datetime
import random
from configurations import credentials,playlist

DAY = 86400 #day in seconds
MIN_DAY_PLAY_DURATION = 30856 # 8hr 34m 16s
MAX_DAY_PLAY_DURATION = 72013 # 20hr 13s
BREAK_DURATION = 14400 # 4hr spread over 3 times a day
PLAY_TIME_DURATION = 30 # 30s

DAILY_DURATIONS = [MIN_DAY_PLAY_DURATION,MAX_DAY_PLAY_DURATION]

SCOPE = 'user-library-read, user-read-playback-state, user-modify-playback-state'


# ATHORIZATION FLOW TO GENERATE TOKEN
OAUTH = SpotifyOAuth(scope=SCOPE, client_id = credentials["CLIENT_ID"], client_secret = credentials["CLIENT_SECRET"])
sp = spotipy.Spotify(auth_manager= OAUTH)


def generate(start,end):
    return random.randInt(start,end)


def random_daily_playtime():
    generate(-1,len(DAILY_DURATIONS))


def get_current_time(): ##return time in seconds
    seconds = datetime.today().timestamp()
    return seconds


def play_playlist(playlist_type = "user", playlist,playlist_length):
    if playlist_type == "user":
        for ids in playlist["PLAYLIST_IDS"]:
            playlistID = f"spotify:user:{credentials["USERNAME"]}:playlist:{ids}"
            sp.start_playback(context_uri=playlistID)
            cp = sp.currently_playing() #find the song playings duration 
            print("first",cp['progress_ms'])
            check_song_progress(cp,random_states) # randomise playing state
    else:
        for ids in playlist["ARTIST"]:
            #play here
            playlistID = f"spotify:artist:{ids}"
            sp.start_playback(context_uri=playlistID)
            #play time to  you can use sleep


def check_song_progress(cp,random_states):
    if cp['progress_ms'] >= 1000 and cp['progress_ms'] <= 15000: #check progress between 1s and 15s
        state = generate(-1,2)
        if random_states[state]:
            time.sleep(30)
            sp.next_track()


daily_playtime = generate(-1,2)
daily_count_down = DAILY_DURATIONS[daily_playtime]


max_break_time = 7200 # 2 hours
break_time_count = 3 #3 times a day
break_time_counter = 0


start_time = get_current_time() #get time in seconds
end_time = current_time+daily_count_down

playlist_ids = len(playlist["PLAYLIST_IDS"]) 
artist_ids = len(playlist["ARTIST"]) 


random_break = generate(0,max_break_time)
random_break_start = get_current_time() #we can use  start_time
random_break_end = random_break_start+random_break
#reduce break time count


#play duration before sleep time or break kick's in
play_duration = end_time/random_break_end #


random_states = [True,False]




if start_time != end_time:
    if start_time != play_duration and play_duration > PLAY_TIME_DURATION: #making sure we dont have  short play durations less done 30 secs
        if playlist_ids != 0 and artist_ids != 0:
            for ids in playlist["PLAYLIST_IDS"]:
                playlistID = f"spotify:user:{credentials["USERNAME"]}:playlist:{ids}" #play song
                sp.start_playback(context_uri=playlistID)
                cp = sp.currently_playing() #find the song playings duration 
                print("first",cp['progress_ms'])
                check_song_progress(cp,random_states) # randomise playing state
                # if PLAY_TIME_DURATION >= break_time_counter:
                #     #choose to play next truck or take break
            for ids in playlist["ARTIST"]:
                #play here
                playlistID = f"spotify:artist:{ids}"
                sp.start_playback(context_uri=playlistID)
                #play time to  you can use sleep
        
        if playlist_ids != 0 and artist_ids == 0:
            break_time_counter += 1
            play_playlist(playlist_type="user",playlist=playlist["PLAYLIST_IDS"], playlist_length= len(playlist["PLAYLIST_IDS"]))
    
        if playlist_ids == 0 and artist_ids != 0:
            break_time_counter += 1
            play_playlist(playlist_type="user",playlist=playlist["ARTIST"], playlist_length= len(playlist["ARTIST"]))

    else:
        sp.pause_playback()
        time.sleep(random_break_end)
        BREAK_DURATION -= random_break_end #break_time_left
        break_time_counter += 1 #increamet counter to meet count value
        if break_time_counter == break_time_count:
            play_duration_left = end_time -play_duration #get remaing play time
            play_duration = play_duration_left
        #else continue
        

else:
    sp.pause_playback()    



