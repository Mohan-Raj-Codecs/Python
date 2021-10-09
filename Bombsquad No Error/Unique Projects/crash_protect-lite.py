#Server Protection By Nippy#2677
#Credits : UnKnowNLeGenD#6715
import ba
import _ba
from urllib.request import urlopen
import json, threading
from datetime import date

def kicker(i):
    url = "http://bombsquadgame.com/accountquery?id="+str(i['account_id'])
    data = json.loads(urlopen(url).read())
    try: created = data['created']
    except: return
    today = date.today()
    created = date(int(created[0]), int(created[1]), int(created[2]))
    day = (today-created).days
    if day <= 6: _ba.disconnect_client(i['client_id'])

def kicks():
    for i in _ba.get_game_roster():
        t = threading.Thread(target=kicker,args=[i])
        t.start()


def protect():
    """
    Call this Function anywhere
    to invoke Security scan for Infinite Times
    """
    ba.timer(0.1, kicks, repeat=True)
