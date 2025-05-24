import time
import random
import pyautogui as pg
from colorama import Fore

print(Fore.GREEN + '''
▄▄▌ ▐ ▄▌ ▄ .▄ ▄▄▄· ▄▄▄▄▄.▄▄ ·  ▄▄▄·  ▄▄▄· ▄▄▄·    .▄▄ ·  ▄▄▄· ▄▄▄· • ▌ ▄ ·. • ▌ ▄ ·. ▄▄▄ .▄▄▄  
██· █▌▐███▪▐█▐█ ▀█ •██  ▐█ ▀. ▐█ ▀█ ▐█ ▄█▐█ ▄█    ▐█ ▀. ▐█ ▄█▐█ ▀█ ·██ ▐███▪·██ ▐███▪▀▄.▀·▀▄ █·
██▪▐█▐▐▌██▀▐█▄█▀▀█  ▐█.▪▄▀▀▀█▄▄█▀▀█  ██▀· ██▀·    ▄▀▀▀█▄ ██▀·▄█▀▀█ ▐█ ▌▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌██▌▐▀▐█ ▪▐▌ ▐█▌·▐█▄▪▐█▐█ ▪▐▌▐█▪·•▐█▪·•    ▐█▄▪▐█▐█▪·•▐█ ▪▐▌██ ██▌▐█▌██ ██▌▐█▌▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪▀▀▀ · ▀  ▀  ▀▀▀  ▀▀▀▀  ▀  ▀ .▀   .▀        ▀▀▀▀ .▀    ▀  ▀ ▀▀  █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀ .▀  ▀
                                                                                                                                                                                                                                                                          
          [1] START (for spam press enter after 10 seconds)                                                                                                                          ''' + Fore.RESET)

choice = input()

if choice == '1':
  message = ['test1', 'test2', 'test3']
  time.sleep(0.10)
  print(Fore.RED + 'Preparing in 10 seconds...' + Fore.RESET)
  for i in range(50):
    msg = random.choice(message)
    pg.write(msg)
    pg.press('enter')
else:
 print('INVALID INPUT')
