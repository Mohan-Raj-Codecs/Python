import ba
import _ba
from urllib.request import urlopen
import json
import datetime
from datetime import date
import threading

def kicker(i):
    url = "http://bombsquadgame.com/accountquery?id="+str(i['account_id'])
    data = json.loads(urlopen(url).read())
    try: created = data['created']
    except: return
    today = str(datetime.datetime.now())[:10].split('-')
    today = (int(today[0]), int(today[1]), int(today[2]))
    day = str(date(today[0], today[1], today[2]) - date(created[0],created[1],created[2])).split()[0]
    try: day = int(day)
    except: day = 0
    if day <= 5: _ba.disconnect_client(i['client_id'])

def kicks():
    for i in _ba.get_game_roster():
        t = threading.Thread(target=kicker,args=[i])
        t.start()


def server_protect():
    ba.timer(0.1, kicks, repeat=True)