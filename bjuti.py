import sys
import tkinter as tk
import math
from tkinter.scrolledtext import ScrolledText

class Booking:
    def __init__(self, booking):
        self.booking = booking.split()
        
        self.ref = self.booking[(self.booking.index('Ref.:')) + 1]        
        self.date = self.booking[(self.booking.index('Date:')) + 1]        
        self.time = self.booking.index('Time:')        
        self.time = {
            'start':self.booking[self.time + 1].replace(':', ""),
            'end':self.booking[self.time + 3].replace(':', ""),
            'duration':int(self.booking[self.time + 6])
        }
        self.capacity = self.booking[self.booking.index('Capacity:') + 1]        
        self.station = self.booking[self.booking.index('Station:') + 1]
        
    def durCheck(self):
        timeDif = math.floor(((int(self.time['end']) - int(self.time['start'])) / 100) * 60)
        
        if timeDif != self.time['duration']:
            print('o chuj!')
        else:
            print('prima!') 
           
    print(dir())
        
class CreateProject:
    def __init__(self, master):
        self.master = master
        
        self.canvas = tk.Canvas(master, width = 800, height = 600)
        self.canvas.pack()
        
        self.textFrame = ScrolledText(self.master, width=100, bd=10, relief="raised")
        self.textFrame.pack()
        # Added for testing.
        self.save_btn = tk.Button(self.master, text="Create", width=25, height=2, bg="green", fg="white", command=self.save)
        self.save_btn.pack()
        
        self.canvas.create_window(400, 280, height= 500, width = 600, window=self.textFrame)
        self.canvas.create_window(200, 565, height= 50, width = 100, window=self.save_btn)

    def save(self):
        self.saveText = self.textFrame.get('1.0', tk.END)  # Get all text in widget.
        self.booking = Booking(self.saveText)    
        
    def create(self):
            

root = tk.Tk()
project = CreateProject(root)
root.mainloop()