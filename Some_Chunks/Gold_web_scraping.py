from bs4 import BeautifulSoup as bs
import requests as req
import time

def conect():
    try:
        source=req.get('https://www.google.com/search?safe=active&rlz=1C1CHBF_enIN932IN932&sxsrf=ALeKk00qFKlhdvMUsZW6iZQITysbLcyqbA%3A1608809618388&ei=knzkX--QF5rqz7sPkaaIqAM&q=gold+rate+today+one+gram+in+chennai&oq=gold+rate+today+one+gram+in+chennai&gs_lcp=CgZwc3ktYWIQAzIJCAAQyQMQFhAeMgYIABAWEB46BAgAEEc6BQgAEMkDOgIIAFCl4X1Y1-59YJvxfWgAcAJ4AIABnQGIAY8MkgEEMC4xMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjvocLuwubtAhUa9XMBHRETAjUQ4dUDCA0&uact=5').text
    except : #No Internet Handling
        print("Please Connect to internet : ( \n\n")
        print("Retrying in 5")
        time.sleep(1)
        print("Retrying in 4")
        time.sleep(1)
        print("Retrying in 3")
        time.sleep(1)
        print("Retrying in 2")
        time.sleep(1)
        print("Retrying in 1")
        time.sleep(1)
        print("Retrying .........................\n\n")
        conect()
    try:
        soup=bs(source,'lxml')
    except UnboundLocalError :   #Assignment Error Handling
        source=req.get('https://www.google.com/search?safe=active&rlz=1C1CHBF_enIN932IN932&sxsrf=ALeKk00qFKlhdvMUsZW6iZQITysbLcyqbA%3A1608809618388&ei=knzkX--QF5rqz7sPkaaIqAM&q=gold+rate+today+one+gram+in+chennai&oq=gold+rate+today+one+gram+in+chennai&gs_lcp=CgZwc3ktYWIQAzIJCAAQyQMQFhAeMgYIABAWEB46BAgAEEc6BQgAEMkDOgIIAFCl4X1Y1-59YJvxfWgAcAJ4AIABnQGIAY8MkgEEMC4xMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjvocLuwubtAhUa9XMBHRETAjUQ4dUDCA0&uact=5').text
        soup=bs(source,'lxml')
    return soup
    
def gold():
    soup=conect()
    try :
        sou=soup.find('h3',class_='zBAuLc').text
        print(sou,"\n\n")
        money_with_comma = sou[sou.find(':')+2 : sou.find('INR')] #+2 for eliminating gap
        money_per_10g = int(money_with_comma[0 : money_with_comma.find(',')]+money_with_comma[money_with_comma.find(',')+1:]) #+1 for eliminating , from $
    except :
        print("Your Algorithm has Fault Re-Check it or the Website is Re-aligned in Different order")
        time.sleep(4)
        exit()
    money_per_g= money_per_10g/10
    money_per_8g = money_per_g * 8
    print("1 Sovereign : ₹",int(money_per_8g))
    
    if money_per_8g < 38000 :
        print("\n\n\n\n\nToday is Best to Buy Gold!    :  )  ")
    else :
        print("\n\n\n\n\nNo Luck Today : (")
    time.sleep(10)
    
gold()
