import os
print('Hello you can chat with me with your requirements' )
print('Please keep in mind that for now I am in my developing phase so I only understand english')
while True:
  print('Tell me what you want me to do:' , end='' ) 
  p=input()
  
 

  if(("run" in p) or ("open" in p)) and ("chrome" in p):
    os.system("chrome")
  elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("media" in p) and ("player" in p)):
      os.system("wmplayer")
  elif(("run" in p) or ("open" in p) or ("execute" in p)) and ("arduino" in p):
    os.system("Arduino")
  elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("whatsapp" in p) or ("messenger" in p )):
    os.system("chrome whatsapp.com")
  elif(("run" in p) or ("open" in p) or ("execute" in p)) and (("calculator" in p) or ("calculate" in p ) or ("calci" in p)):
    os.system("calc")
  elif(("open" in p) or ("run" in p)) and (("microsoft" in p) or ('ms' in p)) and ("teams" in p):
     os.system("chrome microsoftteams.com")
  elif("open"in p) and ("camera" in p):
    os.system(' start microsoft.windows.camera:')  
  elif("open"in p) and ("calander" in p):
    os.system(' start outlookcal:')
  elif("open"in p) and ("maps" in p):
    os.system(' start bingmaps:')  
  elif(("open" in p) or ("set" in p)) and (("clock" in p) or ("alarm" in p)):
     os.system(' start ms-clock:')
  elif("open"in p) and ("skype" in p):
    os.system(' start skype:')
  elif("open" in p) and((("voice" in p) and ("recorder" in p)) or ('recorder' in p)):
    os.system('start ms-callrecording:')
  elif("weather" in p) or (("weather" in p) and ("today" in p) ):
      os.system('start bingweather:')
  elif  ("exit" in p)  or ("quit" in p):
	  break
  else:
     print("Sorry I don't support it right now, will work on it for sure")