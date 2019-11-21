from tkinter import *
import datetime
from random import randint
import time

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("Magic Mirror")
        self.tk.configure(bg="black")
        self.tk.attributes('-zoomed', True)
        
        self.time_date_frame = Frame(self.tk, bg = "black")
        self.time_date_frame.pack(fill = X)
        
        self.date_display = Label(self.time_date_frame, font = ("", 40), bg = "black", fg = "white")
#        self.date_display.grid(row = 0, column = 2, sticky = E)
        self.date_display.pack(anchor = "w")
#        self.date_display.columnconfigure(2, weight = 1)

        self.time_display = Label(self.time_date_frame, font = ("", 40), bg = "black", fg = "white")
#        self.time_display.grid(row = 0, column = 0, sticky = W)
        self.time_display.pack(anchor = "w")
#        self.time_display.columnconfigure(0, weight = 1)

#        self.time_date_frame.grid_columnconfigure(1, weight = 1)
#        self.time_date_frame.grid_rowconfigure(1, weight = 1)
        
        self.coin = Frame(self.tk, bg = "black")
        self.coin.pack(fill = X)
        
        self.coin_display = Label(self.coin, font = ("", 40), bg = "black", fg = "white")
        self.coin_display.pack(anchor = "center")
        
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        
        self.show_date = False
        self.update_date()
        
        self.show_clock = False
        self.update_clock()
        
        self.hide_cover = True
        
        
        
        
        # DONE
        # "mirror mute" => starts listening to commands
        # "mirror unmute" => stops listening to commands
        
        # "mirror wake up" or "mirror sleep"
        #self.toggle_cover()
        
        # "flip a coin"
        #self.flip_a_coin()
        
        # "show clock" or "hide clock" 
        self.toggle_clock()
        
        # "show date" or "hide date"
        self.toggle_date()
        
        # TODO
        # "what's the weather like" => displays weather
        # "hide weather" => hides the weather
        
        # "what's in the news today" => displays the news
        # "hide news" => hides the news
        
        # "play ..." open chrome in background and display "Playing video_name"
        # "stop playing" close chrome and hide "Playing video_name"
        
    def toggle_cover(self):
        color = "black" if self.hide_cover else "white"
        self.hide_cover = not self.hide_cover
        
        self.date_display.config(fg = color)
        self.time_display.config(fg = color)
        self.coin_display.config(fg = color)
        
    def toggle_clock(self):
        self.show_clock = not self.show_clock
        self.update_clock()
    
    def toggle_date(self):
        self.show_date = not self.show_date
        self.update_date()
        
    def flip_a_coin(self):
        result = "Heads" if randint(0, 1) == 0 else "Tails"
        self.coin_display.config(text = result)
        self.tk.after(5000, lambda: self.coin_display.config(text = ""))
        
    def update_clock(self):
        if self.show_clock:
          time = datetime.datetime.now().strftime('Time: %H:%M:%S')
          self.time_display.config(text = time)
        else:
          self.time_display.config(text = "")
            
        self.tk.after(1000, self.update_clock)
        
    def update_date(self):
        if self.show_date:
          date = datetime.datetime.now().strftime('Date: %d/%m/%y')
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

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()
