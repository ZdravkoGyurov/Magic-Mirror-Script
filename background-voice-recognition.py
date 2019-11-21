import time
import weather
import youtube_util
import google_util
import speech_recognition as sr
from random import randint
from datetime import datetime
import os

listen = True

def stop_listening():
  listening(wait_for_stop=False)

def callback(recognizer, audio):
  try:
    command = recognizer.recognize_google(audio)

    global listen
    
    if(command == "what's in the news today" and listen == True):
      google_util.get_news()
      return

    if(command.split(" ", 1)[0] == "play" and listen == True):
      youtube_util.play_video(command.split(" ", 1)[1])
      return

    if(command == "what's the time" and listen == True):
      print(datetime.now().strftime('%H:%M:%S'))
      return

    if(command == "what date is it" and listen == True):
      print(datetime.now().strftime('%d-%m-%Y'))
      return

    if(command == "flip a coin" and listen == True):
      print("Heads" if randint(0, 1) == 0 else "Tails")
      return

    if(command == "what's the weather like" and listen == True):
      weather.run()
      return

    if(command == "mirror wake up" and listen == False):
      listen = True
      print("Started listening...")
      return

    if(command == "mirror sleep" and listen == True):
      listen = False
      print("Stopped listening")
      return

#    if listen == True:
#      print(command)
  except sr.UnknownValueError:
    return
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
os.system('clear')

with m as source:
  r.adjust_for_ambient_noise(source)

listening = r.listen_in_background(m, callback)

# do some stuff
while True: time.sleep(0.1)

# stop listening
#listening(wait_for_stop=False)

# do more stuff
#while True: time.sleep(0.1)
