import sys
import tkinter as tk
import math
from tkinter.scrolledtext import ScrolledText
import createBooking
import outlook


class Booking:
    def __init__(self, booking):
        self.booking = booking.split()
        self.booking = [item.lower() for item in self.booking]

        self.ref = self.booking[(self.booking.index('ref.:')) + 1] if 'ref.:' in self.booking else 'brak ref' 

        self.date = self.booking[(self.booking.index('date:')) + 1]        
        self.time = self.booking.index('time:')

        self.time = {
            'start' : str(int(self.booking[self.time + 1].replace(':', "")) + 200),
            'end' : str(int(self.booking[self.time + 3].replace(':', "")) + 200),
            'duration' : int(self.booking[self.time + 6])
        }
        self.capacity = self.booking[self.booking.index('capacity:') + 1]   
        
        self.start_index = self.booking.index('station:')
        self.end_index = self.booking.index('uplink:') - 1
        self.station = ''

        while not (self.start_index == self.end_index):  
            self.start_index += 1          
            self.station = self.station + self.booking[self.start_index]
        
        self.station = self.station.upper().replace('-','')

        self.receivedTime = '[' + str(self.booking[(self.booking.index('receivedtime:')) + 1]) + ' ' + str(self.booking[(self.booking.index('receivedtime:')) + 2]) + ']'
        self.receivedTime = self.receivedTime[:19]
        
    def durCheck(self):
        timeDif = math.floor(((int(self.time['end']) - int(self.time['start'])) / 100) * 60)
        
        if timeDif != self.time['duration']:
            print('o chuj!')
        else:
            print('prima!')
        
class CreateProject:
    def __init__(self, master):
        self.master = master
        
        self.canvas = tk.Canvas(master, width = 800, height = 600)
        self.canvas.pack(fill='both')

        self.listbox = tk.Listbox(self.master, width=100, bd=10, relief="raised")
        self.listbox.pack()

        self.refresh()

        self.save_btn = tk.Button(self.master, text="Create", width=25, height=2, bg="green", fg="white", command=self.save)
        self.save_btn.pack()

        self.refresh_btn = tk.Button(self.master, text="Refresh", width=25, height=2, bg="orange", fg="white", command=self.refresh)
        self.refresh_btn.pack()
        
        self.canvas.create_window(400, 280, height= 500, width = 600, window=self.listbox)
        self.canvas.create_window(200, 565, height= 50, width = 100, window=self.save_btn)
        self.canvas.create_window(600, 565, height= 50, width = 100, window=self.refresh_btn)

    def refresh(self):
        self.listbox.delete(0, tk.END)

        self.messages = outlook.getMail()
        self.messages = self.messages.currentBookings

        for mail in self.messages:
            self.msg_format = str(mail.sender) + ' TOPIC: ' + mail.Subject + ' ' + str(mail.ReceivedTime.date()) + ' ' + str(mail.ReceivedTime.hour) + ':' + str(mail.ReceivedTime.minute)
            self.listbox.insert(tk.END, self.msg_format)

    def save(self):
        self.selection = self.listbox.curselection()[0]
        self.saveText = self.messages[self.selection].body + ' receivedtime: ' + str(self.messages[self.selection].ReceivedTime)
        print(self.messages[self.selection].ReceivedTime)
        self.booking = Booking(self.saveText)
        createBooking.create(self.booking)
    
root = tk.Tk()
project = CreateProject(root)
root.mainloop()

