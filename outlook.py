
import sys, win32com.client, datetime, re
from tkinter import *

class getMail:
  def __init__(self):
    self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    self.messages = self.outlook.Folders['Coordination@tvn.pl'].Folders['Skrzynka odbiorcza'].Items
    self.messages.Sort("[ReceivedTime]", True)
    self.currentDate = str(datetime.date.today())
    self.keyword = 'GMLinks'
    self.currentBookings = []

    for mail in self.messages:
      mail_date = str(mail.ReceivedTime)
      mail_sender = str(mail.sender)

      if re.search(self.keyword, mail_sender):
        subject = str(mail.Subject).lower()

        if not re.search('re:', subject):
          self.currentBookings.append(mail)

      elif not re.search(self.currentDate, mail_date):
        break
