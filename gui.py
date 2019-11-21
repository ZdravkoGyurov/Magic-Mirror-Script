from tkinter import *
import datetime
from random import randint
import time
import weather
import google_util

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Magic Mirror")
        self.tk.configure(bg="black")
        self.tk.attributes('-zoomed', True)
        
        self.top_frame = Frame(self.tk, bg = "black")
        self.top_frame.pack(fill = BOTH, anchor = "n")
        
        self.time_date_frame = Frame(self.top_frame, bg = "black")
        self.time_date_frame.pack(side = LEFT, anchor = "n")
        
        self.date_display = Label(self.time_date_frame, font = ("", 36), bg = "black", fg = "white")
        self.date_display.pack()
        self.time_display = Label(self.time_date_frame, font = ("", 36), bg = "black", fg = "white")
        self.time_display.pack()

        self.coin = Frame(self.tk, bg = "black")
        self.coin.pack(fill = X)
        self.coin_display = Label(self.coin, font = ("", 40), bg = "black", fg = "white")
        self.coin_display.pack(anchor = "center")
        
        self.mute_unmute = Frame(self.tk, bg = "black")
        self.mute_unmute.pack(fill = X)
        self.mute_unmute_display = Label(self.mute_unmute, font = ("", 40), bg = "black", fg = "red")
        self.mute_unmute_display.pack(anchor = "center")
        
        self.weather_display = Label(self.top_frame, font = ("", 24), bg = "black", fg = "white")
        self.weather_display.pack(anchor = "ne", side = RIGHT)
        
        self.news = Frame(self.tk, bg = "black")
        self.news.pack(anchor = "sw", side = LEFT)
        self.news_display = Label(self.news, font = ("", 14), bg = "black", fg = "white", anchor = SW)
        self.news_display.pack()
        
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        
        self.hide_cover = True
        self.show_date = False
        self.show_clock = False
        self.show_weather = False
        self.show_news = False
        self.show_mute = False
        
        self.update_date()
        self.update_clock()
        
        # DONE
        # "mirror mute" => starts listening to commands
        # "mirror unmute" => stops listening to commands
        
        # DONE
        # "mirror wake up" or "mirror sleep"
        #self.toggle_cover()
        # DONE
        # "flip a coin"
        #self.flip_a_coin()
        # DONE
        # "show clock" or "hide clock" 
        #self.toggle_clock()
        # DONE
        # "show date" or "hide date"
        #self.toggle_date()
        # DONE
        # "show weather" or "hide weather"
        #self.toggle_weather()
        # "what's in the news today" or "hide news"
        #self.toggle_news()
        
        # TODO
        # "play ..." open chrome in background and display "Playing video_name"
        # "stop playing" close chrome and hide "Playing video_name"
        
    def toggle_cover(self):
        color = "black" if self.hide_cover else "white"
        self.hide_cover = not self.hide_cover
        
        self.date_display.config(fg = color)
        self.time_display.config(fg = color)
        self.coin_display.config(fg = color)
        self.weather_display.config(fg = color)
        self.news_display.config(fg = color)
        
    def toggle_mute(self):
        self.show_mute = not self.show_mute
        
        if self.show_mute:
            self.mute_unmute_display.config(text = "not listening")
        else:
            self.mute_unmute_display.config(text = "")
        
    def toggle_news(self):
        self.show_news = not self.show_news
        
        if self.show_news:
            google_util.get_news()
            file = open("news_report.txt", "r")
            news_report = file.read()
            self.news_display.config(text = news_report)
        else:
            self.news_display.config(text = "")
        
    def toggle_weather(self):
        self.show_weather = not self.show_weather
        
        if self.show_weather:
            weather.run()
            file = open("weather_report.txt", "r")
            weather_report = file.read()
            self.weather_display.config(text = weather_report)
        else:
            self.weather_display.config(text = "")
        
    def toggle_clock(self):
        self.show_clock = not self.show_clock
        self.update_clock()
    
    def toggle_date(self):
        self.show_date = not self.show_date
        self.update_date()
        
    def flip_a_coin(self):
        result = "heads" if randint(0, 99) % 2 == 0 else "tails"
        self.coin_display.config(text = result)
        self.tk.after(2500, lambda: self.coin_display.config(text = ""))
        
    def update_clock(self):
        if self.show_clock:
          time = datetime.datetime.now().strftime('time: %H:%M:%S')
          self.time_display.config(text = time)
        else:
          self.time_display.config(text = "")
            
        self.tk.after(1000, self.update_clock)
        
    def update_date(self):
        if self.show_date:
          date = datetime.datetime.now().strftime('date: %d/%m/%y')
          self.date_display.config(text = date)
        else:
          self.date_display.config(text = "")
          
        self.tk.after(60000, self.update_date)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

#if __name__ == '__main__':
#    w = Fullscreen_Window()
#    w.tk.mainloop()
