import requests, threading; from pystyle import *; from os import system;import httpx; import random

# Setup 
system("title Amaterasu - Azulax#0511")
System.Size(140,30)
white = Col.white
red = Col.light_green
purple = Col.light_blue
faild = 0
scc = 0
sent = 0
lock = threading.Lock()
# Setup

def Body():
    try:
        system("cls")
    except:
        system("clear")
    banner = """


                                            ▄▄▄· • ▌ ▄ ·.  ▄▄▄· ▄▄▄▄▄▄▄▄ .▄▄▄   ▄▄▄· .▄▄ · ▄• ▄▌
                                            ▐█ ▀█ ·██ ▐███▪▐█ ▀█ •██  ▀▄.▀·▀▄ █·▐█ ▀█ ▐█ ▀. █▪██▌
                                            ▄█▀▀█ ▐█ ▌▐▌▐█·▄█▀▀█  ▐█.▪▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▄▀▀▀█▄█▌▐█▌
                                            ▐█ ▪▐▌██ ██▌▐█▌▐█ ▪▐▌ ▐█▌·▐█▄▄▌▐█•█▌▐█ ▪▐▌▐█▄▪▐█▐█▄█▌
                                            ▀  ▀ ▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀▀  ▀▀▀ 
                                                            Made by Azulax#0511

    """
    print(Colorate.Vertical(Colors.blue_to_green, banner, 4))
Body()

url = Write.Input("link Graber -> ", Colors.purple_to_blue, interval=0.02)
thread = Write.Input("Thread -> ", Colors.purple_to_blue, interval=0.02)
Proxye = Write.Input("Proxy list -> ", Colors.purple_to_blue, interval=0.03)
def proxy_list():
    with open(Proxye, "r+")as f:
        pro = random.choice(f.readlines())
        f.close()
        return pro


def Star():
    global scc
    global sent
    global faild
    sent += 1
    try:
        httpx.post(url,headers={'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",     'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',}, proxies={"http://": "http://"+proxy_list(), "https://": "http://"+proxy_list()})
        lock.acquire()
        scc += 1
        lock.release()
    except:
        lock.acquire()
        faild += 1
        lock.release()


def Amaterasu():
    Body()

    for i in range(int(thread)):
        threading.Thread(target=Star).start()
        print(f"{purple}Sent -> {red}{sent}  {white}|  {purple}Failed -> {red}{faild}  {white}|  {purple}succes -> {red}{scc}", end="\r")
    print("\n")
    Write.Input("[!] Finished ", Colors.green_to_red, interval=0.03)
Amaterasu()
