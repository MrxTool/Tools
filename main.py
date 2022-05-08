import socket
import time as rnd
from termcolor import colored as color
import datetime 
import sys
from login import Login
import os

rnd.sleep(7)
os.system("clear")
bold = "\033[1m"
ends = "\033[0m"
print(color("—", "red")*50)
print(color("—", "red"),color("                    TOOLS                     ", "green"),color("—", "red"),)
print(color("—", "red")*50)
timed = datetime.datetime.now()
print(color("—", "red"),color("Date    :", "blue"),timed.strftime("%X"),color("    —", "red"), color("Status:", "blue"), color("Online", "green"),color("       —", "red"))
print(color("—", "red"),color("Time    :", "blue"),timed.strftime("%x"),color("    —", "red"), color("Version:","blue"),color("Premium", "yellow"),color("     —", "red"))
print(color("—", "red")*50)
print(color("—", "red"),color("Created: ", "yellow"),bold,color("Cryptix", "green"),ends)
print(color("—", "red")*50)

print(color("                      LOGIN", "green"))
print(color("—", "red")*50)

try:
 username = str(input("Username: "))
 password = input("Password: ")
 if username == Login.userr and password == Login.passs:
   rnd.sleep(7)
   os.system("clear")
   import load
 else:
   for animations in "          Username and password wrong!\n":
     red = "\033[91m"
     end = "\033[0m"
     sys.stdout.flush()
     sys.stdout.write(red+animations+end)
     rnd.sleep(.1)
except:
  pass
#end
