import time
import weather
import youtube_util
import google_util
import speech_recognition as sr
from random import randint
from datetime import datetime
import os
import gui

listen = True

def stop_listening():
  listening(wait_for_stop=False)

def callback(recognizer, audio):
  try:
    command = recognizer.recognize_google(audio).lower()
    print(command)

    global listen
    
    if(command == "mirror news" and listen == True):
      w.toggle_news()
      return
  
    if((command == "mirror wake up" or command == "mirror sleep") and listen == True):
        w.toggle_cover()
        return

    if(command.split(" ", 1)[0] == "play" and listen == True):
      youtube_util.play_video(command.split(" ", 1)[1])
      return

    if(command == "mirror flip a coin" and listen == True):
      w.flip_a_coin()
      return
  
    if(command == "mirror clock" and listen == True):
      w.toggle_clock()
      return

    if(command == "mirror date" and listen == True):
      w.toggle_date()
      return

    if(command == "mirror weather" and listen == True):
      w.toggle_weather()
      return

    if(command == "mirror start listening" and listen == False):
      listen = True
      w.toggle_mute()
      print("Started listening...")
      return

    if(command == "mirror stop listening" and listen == True):
      listen = False
      w.toggle_mute()
      print("Stopped listening")
      return
  
  except sr.UnknownValueError:
    return
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()
#os.system('clear')

with m as source:
  r.adjust_for_ambient_noise(source)

listening = r.listen_in_background(m, callback)

# do some stuff
#if __name__ == '__main__':
w = gui.Fullscreen_Window()
w.tk.mainloop()
while True: time.sleep(0.1)

# stop listening
#listening(wait_for_stop=False)

# do more stuff
#while True: time.sleep(0.1)
