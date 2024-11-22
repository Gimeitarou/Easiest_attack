import sys
import os
import time
import subprocess

AutherSigniture = "Written by GIMEITAROU."

#check if there's Signiture.txt or not
if os.path.isfile('Signiture.txt') == False: #if no Signiture.txt
    print("Let's look for your first Honey Pod.\n") #First greeting
    time.sleep(2)
    f = open("Signiture.txt", 'w', encoding='UTF-8')
    f.write(f'{AutherSigniture}') #creates Signiture.txt
    f.close()
    print('Making signiture file...')
    time.sleep(3)
    sys.exit()

#put contents of Signiture.txt into OverWritten
f = open("Signiture.txt", 'r', encoding='UTF-8')
OverWritten = f.read()
f.close

#check if Signiture.txt have been modified or not
if OverWritten != AutherSigniture:
    subprocess.run('color f0 ' #white
                   +'& echo Honey Pod Found !! & timeout 5 > nul '
                   +'& color 0f '#black
                   +"& echo Tasty or not?"
                   +'& timeout 2 > nul'
                   +'& echo Best wishes for your Developer life.'
                   +'& timeout 3 > nul', shell=True)
else:
    print("Honey Pod Not Found.\n")
    time.sleep(2)

#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.