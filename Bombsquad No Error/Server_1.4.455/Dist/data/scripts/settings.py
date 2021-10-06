import bs
enableTop5effects = True
enableTop5commands = True
enableCoinSystem = True

texts = [u'Welcome to \ue047HARLEY QUINN EPIC TEAMS\ue047','Dont Spam And Abuse\n Join Our Discord Server yet_to_be_created','Dont Ask For Admin Ship \nYou Can Buy it.',u'Server Owner : \ue047Harley\ue047 \nServer Editor : \ue043Nippy\ue043','Use "/shop commands" to see commands available to buy.','Use "/shop effects" to see effects available and their price.','Use "/me" or "/stats" to see your '+bs.getSpecialChar('ticket')+' and your stats in this server', 'Use "/buy" to buy effects that you like','Use "/donate" to give some of your tickets to other players','Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']

questionDelay = 60 #seconds
questionsList = {'Who is the owner of this server?': 'harley', 'Who is the editor of this server?': 'nippy',
       'add': None, 
       'multiply': None}

availableCommands = {'/nv': 80, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 250, 
   '/spaz': 50, 
   '/spazall': 380, 
   '/inv': 80, 
   '/invall': 500, 
   '/tex': 70, 
   '/texall': 400, 
   '/freeze': 60, 
   '/freezeall': 580, 
   '/sleep': 280, 
   '/sleepall': 380, 
   '/thaw': 100, 
   '/thawall': 170, 
   '/kill': 800, 
   '/killall': 150, 
   '/end': 100, 
   '/hug': 160, 
   '/hugall': 100, 
   '/tint': 250, 
   '/sm': 500, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 270, 
   '/healall': 570, 
   '/gm': 2900, 
   '/custom': 20000}

availableEffects = {'ice': 5000, 
   'sweat': 750, 
   'scorch': 590, 
   'glow': 490, 
   'distortion': 795, 
   'slime': 590, 
   'metal': 590, 
   'surrounder': 1000}
