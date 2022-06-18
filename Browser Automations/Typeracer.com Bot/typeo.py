from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time as t


d_file='chromedriver.exe'

options = Options()

driver = webdriver.Chrome(d_file,options=options)

def inp():
    inp_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.txtInput')))
    if str(inp_box.get_attribute("disabled"))=="true":
        t.sleep(1)
        inp()
    else:
        return True

driver.get("https://play.typeracer.com/")
Start = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-1"]/a')))
Start.click()
print("Start Clicked\n")


word_wrap = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#gwt-uid-20 > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(1) > td > div > div')))
parts = word_wrap.find_elements_by_css_selector("*")
para=""
if len(parts)>2:
    count=0
    for i in parts:
        if count<=1:
            para+=i.text
        else:
            para+=" "+i.text
        count+=1
else:
    for i in parts:
        para+=" "+i.text
print("Fetched Texts : \n")
print(para)

print("\n\nWaiting For Count Down End......")
while True:
    can_type=inp()
    if can_type:
        break
box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.txtInput')))
print("\nTyping ASAP :)")
box.click()
for i in para:
    box.send_keys(i)
print("\nWon Match :)")
