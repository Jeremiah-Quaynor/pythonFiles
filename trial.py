import time
from datetime import datetime, timedelta
import random 

MIN_DAY_PLAY_DURATION = 60 # 8hr 34m 16s
MAX_DAY_PLAY_DURATION = 240 # 20hr 13s

DAILY_DURATIONS = [MIN_DAY_PLAY_DURATION,MAX_DAY_PLAY_DURATION]
selected_index = random.randrange(0,len(DAILY_DURATIONS))

seconds = datetime.today()
seconds = seconds

count = 0
start = True

breaker= DAILY_DURATIONS[selected_index]/3
stop_time = seconds + timedelta(seconds=DAILY_DURATIONS[selected_index])
first_break= seconds + timedelta(seconds=breaker)
second_break= seconds + timedelta(seconds=(breaker *2))
third_break= seconds + timedelta(seconds=(breaker *3))


print(first_break.time())
print(second_break.time())
print(third_break.time())


# print(seconds.time())
print(stop_time.time())

time.sleep(1)
while start:
    ticker = datetime.today().time()    
    if(ticker.minute <= first_break.minute and ticker.second <= first_break.second):
        print("taking first break")
        break
        # continue
    if((ticker.minute >= first_break.minute and ticker.second >= first_break.second) and (ticker.minute <= second_break.minute and ticker.second <= second_break.second)):
        print("taking second break")
        break
        # continue
    elif((ticker.minute >= second_break.minute and ticker.second >= second_break.second)and (ticker.minute <= third_break.minute and ticker.second <= third_break.second)):
        print("taking third break")
        break
        # continue
    elif(ticker.minute >= third_break.minute and ticker.second >= third_break.second):
        start = False
    print(ticker)
    continue








# while start:
#     ticker = datetime.today().time()    
#     if(ticker.second == stop_time.time().second and ticker.minute == stop_time.time().minute):
#         print("time is up")
#         break
#     else:
#         if(ticker.second == first_break.second and ticker.minute == first_break.minute):
#             print("taking a break")
#             break
            
#     print(f"ticker is: {ticker}")


















    # seconds = datetime.today()
    # seconds = seconds.timestamp()
    # if (seconds < break_time ):
    #     count = count +1 
    #     if( count ==1 ):
    #         print('first break')
    # elif (seconds >= break_time and seconds <= break_time*2) :
    #     count = count +1 
    #     if( count ==2):
    #         print("second break")
    # elif ( seconds >= break_time*2 and seconds <= break_time*3 ):
    #     count = count +1 
    #     if( count == 3):
    #         print("third break")
    # else:
    #     start = False


    







# print(read_time(break_time *3))
