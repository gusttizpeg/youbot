try:
    import webbrowser
    from time import sleep
    import sys
    import os
except ImportError:
    webbrowser = False
except KeyboardInterrupt:
    print("\033[1;31m[!] Exiting.")
    sys.exit()
except:
    print("\033[1;31m[!] Missing webbrowser. Try running python3 -m pip install webbrowser")
    sys.exit()
    
g = "\033[1;32m"
y = "\033[1;33m"
    
os.system("clear")
print(g+"""
_____________________________________________________________________
            ___           _,.---,---.,_
            |         ,;~'             '~;,
            |       ,;                     ;,
   Frontal  |      ;                        ; ,-- Supraorbital Foramen
    Bone    |     ,'                        /'
            |    ,;                       /' ;,
            |    ; ;      .          . <-'  ; |
            |__  | ;   ______       ______   ;<----- Coronal Suture
           ___   |  '/~ ~ . ~ ~\'  |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
 Maxilla,  |      |   |        }:{        | <------ Orbit
Nasal and  |      |   l       / | \       !   |
Zygomatic  |      .~  (__,.-- .^. --.,__)  ~.
  Bones    |      |    ----;' / | \  ;-<--------- Infraorbital Foramen
           |__     \__.       \/^\/       .__
              ___   V| \                 / |V <--- Mastoid Process
              |      | |T~\___!___!___/~T| |
              |      | | IIII_I_I_I_IIII | |
     Mandible |      |  \ III I I I III,/  |
              |       \    ~~~~~~~~~~
              |         \   .       . <-x---- Mental Foramen
              |__         \.    ^    .
                            ^~~~^~~~^
                        Author: Ch33chSec
  _________________________________________________________________
    
    """)
url = input(y+"Enter a youtube url: ")
ref = input(y+"Enter a refresh rate(seconds): ")
browser = input(y+"Enter you default browser: ")
def OpenUrl():
    print("Sucessfully viewed.")
    os.system(" killall -9 " +browser)
    webbrowser.open(url)
    sleep(int(ref))
for i in range(350):
    print(OpenUrl)