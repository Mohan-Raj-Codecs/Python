""" Kicks Newly Created IDS """
# ba_meta require api 6
# Server Protection By Nippy#2677
# Credits : UnKnowNLeGenD#6715

import ba
import _ba
from urllib.request import urlopen
import json, threading
from datetime import date


def get_account_created_date(account_id):
    """ returns date of account creation,
    returns None if account_id is invalid
    """
    try:
        account_url = "http://bombsquadgame.com/accountquery?id="+str(account_id)
        return json.loads(urlopen(account_url).read())['created']
    except: # Sorry The Account ID Is Invalid...
        return

def kick_newly_created_account(account_id: str, client_id: int):
    """
    Kicks Given Account, IF Account Is New.
    Useful When Someone Spams Your Server With New Account.
    -----------------------------------------------------------------------------------------------------------
    Parameters
    -------------------
    account_id: str
        account's account_id, this helps us to check account's data
    
    client_id: int
        account's current client_id. incase if needed, useful when kicking account if it's new.
    ------------------
    """
    account_created_date = get_account_created_date(account_id)
    if account_created_date is None: return
    today_date = date.today()
    account_created_date = date(int(account_created_date[0]), int(account_created_date[1]), int(account_created_date[2]))
    days = (today_date - account_created_date).days
    if days <= 5:
        # Hmm... The Account is new, Let's kick em
        _ba.disconnect_client(client_id)

def check_roster_accounts():
    """
    Checks For Every Account In Roster,
    Using Newly Created Account Kicker Function.
    """
    for i in _ba.get_game_roster():
        t = threading.Thread(target=kick_newly_created_account,args=[i['account_id'], i['client_id']])
        t.start()

def protect():
    """
    protect,
    checks for roster each 0.1 seconds
    """
    ba.timer(0.1, check_roster_accounts, repeat=True)

# ba_meta export plugin
class Protect(ba.Plugin):
    """ My First Ballistica Plugin """
    def __init__(self):
        if _ba.env().get("build_number",0) >= 20246:
            protect()
        else:
            ba.screenmessage("Protector Needs V 1.6 Build greater than 20246",color=(1,0,0))
            print("Protector Needs V 1.6 Build greater than 20246")

print("Nippy Server Protector Ready :)")
