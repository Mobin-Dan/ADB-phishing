import os
from colorama import Fore
import pyfiglet
print(Fore.GREEN)
os.system("clear")
ins =pyfiglet.figlet_format("INstaHack", font="3-d")
print(Fore.RED+ins)
print
print(Fore.GREEN)
print("Goodbye until the next update:)")
os.system("php -S localhost:8090 -t telegram")
