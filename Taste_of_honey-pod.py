import sys
import os
import time
import subprocess

AutherSigniture = "Written by Gimeitarou."

if os.path.isfile('Signiture.txt') == False: #When no Signiture.txt
    print("Let's look for your first Honey Pod.\n") #First greeting
    time.sleep(2)
    f = open("Signiture.txt", 'w', encoding='UTF-8')
    f.write(f'{AutherSigniture}')
    f.close()
    print('Making signiture file...')
    time.sleep(3)
    sys.exit()

#put contents of Signiture.txt into OverWritten
f = open("Signiture.txt", 'r', encoding='UTF-8')
OverWritten = f.read()
f.close

#check if Signiture.txt is overwritten or not
if OverWritten != AutherSigniture:
    subprocess.run('color f0 ' #white
                   +'& echo Found Honey Pod!! & timeout 5 > nul '
                   +'& color 0f '#black
                   +'& echo Tasty or not?'
                   +'& timeout 1 > nul'
                   +'& echo Best wishes for your Red team life!'
                   +'& timeout 3 > nul', shell=True)
else:
    print("Not Found.\n")
    time.sleep(2)


#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.