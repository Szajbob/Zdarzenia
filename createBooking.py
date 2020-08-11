import pyautogui as gui
import pywinauto
import time
from pywinauto.application import Application

gui.PAUSE = 0.4
gui.FAILSAFE = True

def create(booking):
    zdarzenia = Application().connect(title_re=u'Zdarzenia', class_name='SunAwtFrame')
    zdarzenia = zdarzenia.SunAwtFrame
    zdarzenia.set_focus()
    zdarzenia.maximize()    

    gui.click(90, 50)

    time.sleep(0.5)

    gui.press('tab')
    gui.hotkey('ctrl', 'a') 
    gui.write(booking.time['start'])
    print(booking.time['start'])

    gui.press('tab')
    gui.hotkey('ctrl', 'a')
    gui.write(booking.time['end'])
    print(booking.time['end'])

    gui.press('tab')
    gui.write(booking.station)

    gui.press('tab')
    gui.write('S' if booking.capacity == '3.8' else 'D')

    gui.press('tab')
    gui.press('tab')
    gui.press('down')
    gui.press('down')
    gui.press('down')
    gui.press('down')


    gui.press('tab')
    gui.write('Coord')

    gui.press('tab')
    gui.write('Links4Media')

    gui.press('tab')
    gui.press('tab')
    gui.press('space')

    gui.click(600, 625, clicks=2)
    gui.write(booking.ref)

    gui.click(600, 650)
    gui.write(booking.receivedTime)    

    gui.click(600,520)
    gui.hotkey('ctrl', 'a')
    gui.write(booking.date)


