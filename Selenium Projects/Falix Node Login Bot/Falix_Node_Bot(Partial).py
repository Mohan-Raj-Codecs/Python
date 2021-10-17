from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time as t


d_file='chromedriver.exe'

#driver = webdriver.Chrome(d_file)
options = Options()
options.add_extension('VPN.crx')
driver = webdriver.Chrome(d_file,options=options)
#options = Options()
#options.add_argument("user-data-dir=C:\\Users\\raj28\\AppData\\Local\\Google\\Chrome\\User Data\\") 
#driver = webdriver.Chrome(options=options)

#xzIDlgA0xn
#somethingusefull2021@gmail.com
def close_tabs():
    chwd = driver.window_handles
    for w in chwd:
        if(w!=vpn):
            driver.switch_to.window(w)
            driver.close()

    driver.switch_to.window(vpn)

def switch_tabs():
    chwd = driver.window_handles
    for w in chwd:
        if(w!=vpn):
            driver.switch_to.window(w)
    return driver.current_window_handle

def switch_tab(x):
    chwd = driver.window_handles
    for w in chwd:
        if(w==x):
            driver.switch_to.window(w)

def refresh():
    driver.get('https://panel.falixnodes.net/')
    t.sleep(1)

def accept_alert():
    alert = driver.switch_to.alert
    alert.accept()

def VPN_ON(x):
    try:
        ele = driver.find_element_by_xpath('//span[@data-server="'+x+'"]')
        ele.click()
    except:
        VPN_ON(x)

def accept_TC():
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "accept-choices")))
        element.click()
    except:
        pass

def u_enter():
    user = driver.find_element_by_xpath('//input[@name="username"]')
    user.click()
    user.send_keys("somethingusefull2021@gmail.com")

def p_enter():
    user = driver.find_element_by_xpath('//input[@name="password"]')
    user.click()
    user.send_keys("xzIDlgA0xn")

def login():
    logi = driver.find_element_by_xpath('//button[@type="submit"]').click()

def sign_in():
    u_enter()
    p_enter()
    t.sleep(1)
    login()

def ch_server():
    try:
        driver.find_element_by_class_name('sc-1ibsw91-5 gbaFIi').click()
        t.sleep(1)
        driver.find_element_by_class_name('sc-1ibsw91-5 gbaFIi').click()
    except:
        ch_server()

def error_check():
    try:
        error = driver.find_element_by_xpath("//*[text()='Error']")
        accept_TC()
        sign_in()
        error_check()
    except:
        pass



driver.get('https://ipunblock.com/freevpn/')
vpn = driver.current_window_handle
close_tabs()  #closes Unwanted Tabs


try:
    accept_alert()
except:
    pass

VPN_ON('Netherlands (Amsterdam)')
t.sleep(5)


driver.execute_script('''window.open("", "_blank");''')
game_panel = switch_tabs()

refresh()
print("Refrsh 1")
refresh()
print("Refrsh 2")
t.sleep(4)
print("waiting TC")
accept_TC()
print("Accepted TC")
sign_in()

error_check()

t.sleep(20)
print("signed in (Access_Gained)")
atag=driver.find_elements_by_tag_name('a')
server=str(atag[4].get_attribute('href'))
console=server
server=server+'/settings'
print("Grabbing : ",server)
t.sleep(1)
driver.get(server)
t.sleep(10)
switch_tab(vpn)

VPN_ON('Direct Connection')

switch_tab(game_panel)




#Direct Connection
#<span class="sc-1yg9bob-2 fuRqDg title">Error</span>

#<div role="alert" class="sc-1yg9bob-0 sc-1yg9bob-1 ERawl gnROQd"><span class="sc-1yg9bob-2 fuRqDg title">Error</span><span class="sc-1yg9bob-3 iXmoLL">This recaptcha instance did not render yet.</span></div>




#sc-1ibsw91-5 gbaFIi

#selenium.common.exceptions.ElementClickInterceptedException

#<svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="server" class="svg-inline--fa fa-server fa-w-16 " 






#accept-choices
#<input name="username" type="text" class="sc-19rce1w-0 ecQncK" value="">

#Netherlands (Amsterdam)
#<span data-server="Netherlands (Amsterdam)">🇳🇱 Netherlands (Amsterdam)</span>



#driver.quit()

#search = driver



#driver.get  #Opens the URL in Chrome browser
#driver.close()   #Closes a tab that opened
#driver.title      #Returns title of Webpage
#driver.quit()    #Closes entire browser
#driver.page_source   #returns page source

