import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import time
from datetime import datetime
import random
from configurations import credentials,playlist

DAY = 86400 #day in seconds
MIN_DAY_PLAY_DURATION = 30856 # 8hr 34m 16s
MAX_DAY_PLAY_DURATION = 72013 # 20hr 13s
BREAK_DURATION = 14400 # 4hr spread over 3 times a day
PLAY_TIME_DURATION = 30 # 30s


DAILY_DURATIONS = [MIN_DAY_PLAY_DURATION,MAX_DAY_PLAY_DURATION]

SCOPE = 'user-library-read, user-read-playback-state, user-modify-playback-state'
REDIRECT_URL = "https://www.google.com/"


# ATHORIZATION FLOW TO GENERATE TOKEN
OAUTH = SpotifyOAuth(scope=SCOPE, client_id = credentials["CLIENT_ID"], client_secret = credentials["CLIENT_SECRET"],redirect_uri= REDIRECT_URL)
sp = spotipy.Spotify(auth_manager= OAUTH)

# getting device ID
devices = sp.devices()
DEVICE_ID = devices['devices'][0]['id']


def generate(start,end):
    return random.randint(start,end)


def random_daily_playtime():
    daily_playtime = generate(0,len(DAILY_DURATIONS)-1) # btween-1 and 2
    return DAILY_DURATIONS[daily_playtime]

def get_current_time(): ##return time in seconds
    seconds = datetime.today()
    return seconds.timestamp()


def play_playlist(playlist, playlist_type = "user"):
    if playlist_type == "user":
        for ids in playlist:
            user_playlist(ids)
    else:
        for ids in playlist:
            artist_playlist(ids)

def artist_playlist(ids):
    playlistID = f"spotify:artist:{ids}"
    sp.start_playback(device_id=DEVICE_ID, context_uri=playlistID)
    cp = sp.currently_playing() #find the song playings duration 
    # print("progress",cp['progress_ms'])
    print('checking break time')
    check_break_time()
    check_song_progress(cp) # randomise playing state

def user_playlist(ids):
    playlistID = f"spotify:user:{credentials['USERNAME']}:playlist:{ids}"#play song
    sp.start_playback(device_id=DEVICE_ID, context_uri=playlistID)
    cp = sp.currently_playing() #find the song playings duration 
    # print("progress",cp['progress_ms'])
    print('checking break time -user  playlist')
    check_break_time()
    check_song_progress(cp) # randomise playing state


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


def generate_play_duration():
    print("Generating play duration...")
    global play_duration, random_break_end, break_time_counter
    random_break = generate(1800,max_break_time) #between 30mins to 2hrs
    random_break_end = random_break_start+random_break #get time from app start to a random end
    # play_duration = end_time/random_break_end #use the random end to generate a play duration
    play_duration = end_time/3
    print("play duration 1: ", convert(play_duration))
    break_time_counter += 1 #increment counter to meet count value

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


daily_count_down = random_daily_playtime() #get random daily count down duration


max_break_time = 7200 # 2 hours
break_time_count = 3 #3 times a day
break_time_counter = 0

# -------------MAIN START POINT-------------------
print("Program starting...")
start_time = get_current_time() #get time in seconds
end_time = start_time + daily_count_down

playlist_ids = len(playlist["PLAYLIST_IDS"]) 
artist_ids = len(playlist["ARTIST"]) 
print("start time: ",convert(start_time), "end time: ",convert(end_time), "Playlist id: ", playlist_ids, "Artist id: ", artist_ids)


random_break_start = start_time #  the time the app first run
random_break_end = 0

#play duration before sleep time or break kick's in
play_duration = 0
total_play_duration= 0
total_play_duration += play_duration
generate_play_duration()

print("play duration: ", convert(play_duration))




random_states = [True,False]

start = True

def check_break_time():
    global play_duration
    #check if current_time == play_duration + start
    if get_current_time() <= (play_duration+start_time):
        #take a break
        sp.pause_playback()
        print("random_break_end:",convert(random_break_end))
        time.sleep(random_break_end)
        BREAK_DURATION -= random_break_end #break_time_left #reduce total break duration BREAKDURATION
        break_time_counter += 1 #increamet counter to meet count value
        if break_time_counter == break_time_count:
            play_duration_left = end_time - play_duration #get remaing play time
            play_duration = play_duration_left
            print("checking play_duration",convert(play_duration))
        #else continue


while start:
    # start_time != end_time:
    print("checking if daily limit reached...")
    if get_current_time() >= end_time: #always compair the current time with expected daily end time
        #play duration will most likely be smaller than start_time
        print("Play duration :", convert(play_duration+start_time))
        if (play_duration+start_time) > start_time and play_duration > PLAY_TIME_DURATION: #check if play durations > 30 secs
            print("making sure play_duration is no greater than 30s")
            if playlist_ids != 0 and artist_ids != 0:
                print('playing playlist')
                play_playlist(playlist_type="user",playlist=playlist["PLAYLIST_IDS"])
                    # if PLAY_TIME_DURATION >= break_time_counter:
                    #     #choose to play next truck or take break
                print('playing artist')
                play_playlist(playlist_type="artist",playlist=playlist["ARTIST"])
        
            elif playlist_ids != 0 and artist_ids == 0:
                print('Playing playlist only')
                break_time_counter += 1
                play_playlist(playlist_type="user",playlist=playlist["PLAYLIST_IDS"])
        
            elif playlist_ids == 0 and artist_ids != 0:
                print('Playing artist only')
                break_time_counter += 1
                play_playlist(playlist_type="user",playlist=playlist["ARTIST"])
        else:
            #if play_duration < 30s recalculate duration
            # generate_play_duration()
            play_duration += end_time/3
            print("added 30s duration:", convert(play_duration))
    else:
        print('pausing for remaining time')
        sp.pause_playback(device_id=DEVICE_ID)    
        daily_sleep = DAY - daily_count_down #time left after selecting a daily play schedule
        print("pausing for ", convert(daily_sleep))
        time.sleep(daily_sleep)