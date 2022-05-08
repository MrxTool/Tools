import sys
from termcolor import colored as wc
import time as rnd
import platform as oss
import requests
import socket
 
#color
class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
#text to login

for animation in "             WELCOME TO HACKING TOOLS\n":
 sys.stdout.flush()
 sys.stdout.write(Color.GREEN+Color.BOLD+animation+Color.END)
 rnd.sleep(0.1)
#list
for a in "[1] Scan os\n":
 sys.stdout.flush()
 sys.stdout.write(Color.BLUE+a)
 rnd.sleep(.1)
for b in "[2] Dump server\n":
 sys.stdout.flush()
 sys.stdout.write(b)
 rnd.sleep(.1)
for c in "[3] Denial of service\n":
 sys.stdout.flush()
 sys.stdout.write(c)
 rnd.sleep(.1)
for d in "[4] Finding ip address\n":
 sys.stdout.flush()
 sys.stdout.write(d)
 rnd.sleep(.1)
for e in "[5] Hacking facebook target\n":
 sys.stdout.flush()
 sys.stdout.write(Color.BLUE+e+Color.END)
 rnd.sleep(.1)
for f in "[6] Hack gmail\n":
 sys.stdout.flush()
 sys.stdout.write(Color.BLUE+f+Color.END)
 rnd.sleep(.1)
try:
 select_items = int(input(Color.UNDERLINE+"Select=> "+Color.END))
 #os
 if select_items == 1:
   print("Your system: ", oss.system())
  #dump website
 elif select_items == 2:
   host = input("Url: ")
   rnd.sleep(3)
   dumps = requests.get(host)
   print(dumps.text)
 #Denial of service
 elif select_items == 3:
   host_url = input("Url: ")
   port = socket.gethostbyname(host_url)
   for attack in range(1,40000):
     green = Color.GREEN
     end = Color.END
     bold = Color.BOLD
     print(f"{green}Sending {attack} packet to {bold}'%s' {end}" %port)
     rnd.sleep(.1)
 elif select_items == 4:
   hosts = input("Host: ")
   conne = socket.gethostbyname(hosts)
   if conne:
     rnd.sleep(7)
   print(Color.GREEN+f"Ip address: {Color.BOLD}'%s'" %conne,Color.END)
 elif select_items == 5:
   numbers = 1000000000000000000000
   with open("main.exe", "x") as exploits:
    exploits.write("\0" *numbers)
    print("Exploit created")
 elif select_items == 6:
   maks = 1000000000000000000000
   with open("hack.exe", "x") as sq:
     sq.write("\0" *maks)
     print("Hacking")
 elif select_items > 6:
   print(Color.YELLOW+"Not found"+Color.END)
except ValueError:
  print("Only number")
except EOFError:
  pass
except FileExistsError as qw:
  print("File already created")
