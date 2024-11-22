import os
import time
import subprocess

AutherSigniture = "Written by GIMEITAROU."

#make Signiture.txt only when it doesn't exist
if os.path.isfile('Signiture.txt') == False: #check if there's Signiture file or not
    print("Dear bears, look for your first honey-pod.\n") #First greeting
    f = open("Signiture.txt", 'w', encoding='UTF-8')
    f.write(f'{AutherSigniture}')
    f.close()
    print('Making signiture file...')
    time.sleep(3)

#put contents of TEXT.txt into OverWritten
f = open("Signiture.txt", 'r', encoding='UTF-8')
OverWritten = f.read()
f.close

#check if Signiture is overwritten in a specific way
if OverWritten != AutherSigniture:
    subprocess.run('color f0 ' #white
                    +'& echo Found Honey-pod. & timeout 5 > nul '
                    +'& color 0f '#black
                    +'& echo Tasty or not?'
                    +'& echo Happy Red team life, dear.'
                    +'& timeout 3 > nul'
                    +'& ', shell=True)
else:
    print("Seach for first honey-pod.")
    time.sleep(3)

#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.