import discord
import os
import ssh               #Hooking Target Linux System or Server Here
import Permission        #Security Check for Discord Users
import paramiko

client = discord.Client()

# var
Salutation = ['Hello', 'helo', 'Hi', 'hi', 'Yo', 'yo','Helo']
Cong = ['Tq', 'Thank you', 'tq', 'thank you','Thanks', 'thanks', 'thank', 'Thank']
god=[524998197114961921]
# events

@client.event
async def on_ready():
    print('I am Online Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #Local vars
    msgs = str(message.content)[1:]
    msgs = msgs.split(" ")
    msg = msgs[0]
    try:
        args=msgs[1:]
    except:
        args=[]
    for i in args:       #Forcefully removing weeds from List
        try:
            args.remove('')
        except:
            pass
    
    #Decline Private Message Process (To Avoid Misuse)
    #if message.author.id != client.user.id:
     #   if not(message.guild):  # If message in guild
      #      return await message.author.send("I Don't process commands on Direct messages! \n To improve Transparency :slight_smile:")
    #Msg handlers
    if message.author == client.user:
        return
    
    if message.content.startswith('$'):

        if msg=="help":
            await message.channel.send("Check your DM :slight_smile:")
            await message.author.send(file=discord.File('Doc.txt'))

        if msg=="test":                           #Just Code and Test any Commands here
            if not(message.author.id in god) :
                return
            pass

        if msg in Salutation:                     #This is How Normal Bots Work :)
            await message.channel.send("Yo!")
        
        if msg in Cong:
            await message.channel.send("You're Welcome , Always Hope to Serve Better  -bot :slight_smile:")
        
        if msg == "me":
            if Permission.filt(message.author,"owner"):
                await message.channel.send("You're Owner")
            elif Permission.filt(message.author,"admin"):
                await message.channel.send("You're Admin")
            else:
                await message.channel.send("You're Just a Member")
        
        if msg == "list":
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            owners,admins=Permission.lis()
            if owners==[]:
                owners=[None]
            await message.channel.send("Owners : ")
            just=""
            for i in owners :
                just+=str(i)+" , "
            await message.channel.send(just)
            await message.channel.send("Admins : ")
            if admins==[]:
                admins=[None]
            just=""
            for i in admins :
                just+=str(i)+" , "
            await message.channel.send(just)

        if msg == 'status':
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            if ssh.Server_on:
                await message.channel.send('Our Server is Currently Running Up :slight_smile:')
            else:
                await message.channel.send('Our Server is Currently Down :slight_frown:')
        
        if msg == 'start':
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            try:
                if ssh.Server_on:
                    await message.channel.send('Trying to Restart Server')
                else:
                    await message.channel.send('Trying to Start Server')
                ssh.exe("sudo ./start",args[0])
                await message.channel.send('Started Server :slight_smile:')
                ssh.Server_on = True

            except paramiko.ssh_exception.AuthenticationException:
                await message.channel.send('Wrong Password :x:')

            except IndexError:
                await message.channel.send('You Need to Enter the ssh Password after Command :broken_heart: \nExample: $start  pass_word')
            
            except:
                await message.channel.send('There was a Error in Starting Server :slight_frown:')
                await message.channel.send('Try  "$force_start" to start server Ignoring Error') 
                ssh.Server_on = False

        if msg == 'force_start':
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            try:
                await message.channel.send('Trying to Force Start Server ')
                ssh.exe("sudo ./start",args[0])
                await message.channel.send('Started Server :slight_smile:')
                ssh.Server_on = True
            except paramiko.ssh_exception.AuthenticationException:
                await message.channel.send('Wrong Password :x:')
            except IndexError:
                await message.channel.send('You Need to Enter the ssh Password after Command :broken_heart: \nExample: $start  pass_word')
            except:
                await message.channel.send('There was a Error in Starting Server :slight_frown:')
                await message.channel.send("Reason : Can't Contact the Linux Server") 
                ssh.Server_on = False

        if msg == 'stop':
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            try:
                if ssh.Server_on:
                    await message.channel.send('Trying to Stop Server')
                    ssh.exe("sudo ./stop",args[0])
                    await message.channel.send('Stopped Server :slight_smile:')
                    ssh.Server_on = False
                else:
                    await message.channel.send('I Think Server is Already Down')
                    await message.channel.send('Try  $force_stop to stop server Ignoring Error')
            except paramiko.ssh_exception.AuthenticationException:
                await message.channel.send('Wrong Password :x:')
            except IndexError:
                await message.channel.send('You Need to Enter the ssh Password after Command :broken_heart: \nExample: $start  pass_word')
            except:
                await message.channel.send('There was a Error in Stopping Server :slight_frown:')
                await message.channel.send('I can also see that Private server is Currently Down !')
                ssh.Server_on = False
        
        if msg == 'force_stop':
            if not(Permission.filt(message.author,"admin")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            try:
                await message.channel.send('Trying to Force Stop Server')
                ssh.exe("sudo ./stop",args[0])
                await message.channel.send('Stopped Server :slight_smile:')
                ssh.Server_on = False
            except paramiko.ssh_exception.AuthenticationException:
                await message.channel.send('Wrong Password :x:')
            except IndexError:
                await message.channel.send('You Need to Enter the ssh Password after Command :broken_heart: \nExample: $start  pass_word')
            except:
                await message.channel.send('There was a Error in Stopping Server :slight_frown:')
                await message.channel.send("Reason : Can't Contact the Linux Server")
                ssh.Server_on = False
        
        if msg == 'add':
            if not(Permission.filt(message.author,"owner")):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            if len(args)<=1 or len(args)>2:
                await message.channel.send('Less or More Options Passed')
                await message.channel.send('Usage :  $add admin Bot#1234')
            else:
                try:
                    args[1]=Permission.extract_id(args[1])  #extract id if given
                    if type(args[1])==int:
                        try:
                            user = await client.fetch_user(args[1])
                            args[1]=str(user.name)+"#"+str(user.discriminator)
                        except:
                            raise Exception("Can't Fetch user from invalid ID")
                    Permission.ad(args[1],args[0]) #arguments =  user , role
                    await message.channel.send('Added '+str(args[1])+" as Admin")
                except:
                    await message.channel.send("Usage :  $add admin Dummy#1234 or  $add admin @DummyUser")

        if msg == 'remove':
            if not(message.author.id in god):
                await message.channel.send('Permission Denied :slight_frown:')
                return
            if len(args)<=0 or len(args)>1:
                await message.channel.send('Less or More Options Passed')
                await message.channel.send('Usage :  $remove Bot#1234')
            else:
                try:
                    args[0]=Permission.extract_id(args[0])  #extract id if given
                    if type(args[0])==int:
                        try:
                            user = await client.fetch_user(args[0])
                            args[0]=str(user.name)+"#"+str(user.discriminator)
                        except:
                            raise Exception("Can't Fetch user from invalid ID")

                    Permission.rem(args[0])
                    await message.channel.send('Permissions Reclaimed from '+str(args[0]))
                except:
                    await message.channel.send("Can't Reclaim Permissions from "+str(args[0]))





my_secret = ''
client.run(my_secret)
