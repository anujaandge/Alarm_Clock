import time
import datetime
import win32api
import random


class clock:
    def __init__(self) -> None:
        pass
    def current_time(self):
        print("Current time is:")
        print(datetime.datetime.now())
        
    def set_alarm(self):
        invalid = True
 
        while(invalid):
        #Get a valid user input for the alarm time
          print("Set a valid time for the alarm (Ex. 06:30)")
          userInput = input(">> ")
       # For example, this will convert 6:30 to an array of [6, 30].
          alarmTime = [int(n) for n in userInput.split(":")]
    # Validate the time entered to be between 0 and 24 (hours) or 0 and 60 (minutes)
          if alarmTime[0] >= 24 or alarmTime[0] < 0:
                 invalid = True
          elif alarmTime[1] >= 60 or alarmTime[1] < 0:
              invalid = True
          else:
             invalid = False
        
# Number of seconds in an Hour, Minute, and Second
          seconds_hms = [3600, 60, 1]
# Convert the alarm time to seconds
          alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)]) 

          now = datetime.datetime.now()
          currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
          secondsUntilAlarm = alarmSeconds - currentTimeInSeconds
          #5print(type(secondsUntilAlarm))
          if secondsUntilAlarm < 0:
                secondsUntilAlarm += 86400 # number of seconds in a day
 
          print("Alarm is set!")
          print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsUntilAlarm)) 
          time.sleep(secondsUntilAlarm)
          print("Ring Ring... time to wake up!")
          for i in range(0, secondsUntilAlarm):
                   time.sleep(1)
                   #press any key to stop alarm
                   mixer.music.stop()
                   
                   secondsUntilAlarm -= 1
                   print(datetime.timedelta(seconds=secondsUntilAlarm))
                   if(secondsUntilAlarm==00):
                          for i in range(1):
                              win32api.Beep(random.randint(37,10000), random.randint(750,3000))
        snooze_time_in_sec= int(input("enter time in sec:"))
        time_for_snooze = snooze_time_in_sec
        for i in range(3):
            print("repreat after snooze time")
            for i in range(0, snooze_time_in_sec):
                   time.sleep(1)
                   snooze_time_in_sec -= 1
                   print(datetime.timedelta(seconds=snooze_time_in_sec))
                   if(snooze_time_in_sec==0):
                          for i in range(5):
                              win32api.Beep(random.randint(37,10000), random.randint(750,3000))
            snooze_time_in_sec = time_for_snooze
                    
        
           
                              
clock_alarm = clock()
clock_alarm.current_time()
clock_alarm.set_alarm()

        
    
  
