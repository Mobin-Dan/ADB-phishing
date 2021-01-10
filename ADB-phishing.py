import os
import pyfiglet
from colorama import Fore
os.system("unzip insta_hack.zip")
os.system("unzip telenumber.zip")
os.system("clear")
out = pyfiglet.figlet_format("ADB PHIS", font="3-d")
print(Fore.WHITE+"*"*70)
print(Fore.RED+  out)
print(Fore.WHITE+"*"+Fore.GREEN+"[+]"+Fore.RED+"INSTAGRAM")
print(Fore.WHITE+"*"+Fore.GREEN+"[+]"+Fore.RED+"telenumber")
print(Fore.WHITE+"*"*70)
s =input(Fore.RED+"="+Fore.GREEN+"telenumber/instagram"+Fore.RED+">")
if s == "instagram":
        os.system("python module2.py")
if s == "telenumber":
        os.system("python module1.py")
