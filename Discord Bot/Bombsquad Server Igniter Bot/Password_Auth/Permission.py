import json

with open("Permission.json") as dat:
  data=json.load(dat)

def filt(x,y):
  x=str(x)
  y=str(y)
  roll=""
  role=data['roles']
  owners=role['owners']
  admins=role['admins']
  
  if x in owners:
    roll="owner"
  elif x in admins:
    roll="admin"

  if roll=="owner":
    return True
  elif y=="admin":
    if y==roll:
      return True
  elif y==roll:
    return True

  return False

def get_role(x):
  x=str(x)
  role=data['roles']
  owners=role['owners']
  admins=role['admins']
  if x in owners:
    return "owner"
  elif x in admins:
    return "admin"
  else :
    return "member"

def ad(x,y):
  x=str(x)
  y=str(y)
  role=data['roles']
  owners=role['owners']
  admins=role['admins']
  if filt(x,y):
    pass
  elif y=="admin":   #if admin add Owner as admin, Owner Permission Retains :)
    admins.append(x)
  elif y=="owner":
    owners.append(x)
  with open("Permission.json",'w') as dat:
    json.dump(data,dat,indent=2)

def rem(x):
  x=str(x)
  role=data['roles']
  owners=role['owners']
  admins=role['admins']
  if x in admins:
    admins.remove(x)
  if x in owners:
    owners.remove(x)
  with open("Permission.json",'w') as dat:
    json.dump(data,dat,indent=2)

def lis():
  role=data['roles']
  owners=role['owners']
  admins=role['admins']
  return owners,admins

def extract_id(x):
  x=str(x)
  try:
    if x[0]=="<" and x[1]=="@" :     #id to username
      x=list(x)
      del x[0:3]
      del x[len(x)-1]
      x="".join(x)
      x=int(x)
      return x

    x=chk_user(x)
    return x
    
  except:
    raise Exception("This is Not a Username")

  return x
  

def chk_user(x):
  if "#" in x and x[len(x)-4:len(x)].isnumeric():   #checking is it username
    return x
  else:
    raise Exception("This is Not a Username")

#ad("꧁༺Gaylord༻꧂#9494","admin")
#rem("Some#2324")
#print(filt("꧁༺Gaylord༻꧂#9494","admin"))
