import os
import time
import subprocess

TextContents = "This code is written by GIMEITAROU."

#make TEXT.txt only when it doesn't exist
if os.path.isfile('TEXT.txt') == False:
    f = open("TEXT.txt", 'w', encoding='UTF-8')
    f.write(f'{TextContents}')
    f.close()
    print('Wait for a moment...')
    time.sleep(3)

#put contenst of TEXT.txt into OverWritten
f = open("TEXT.txt", 'r', encoding='UTF-8')
OverWritten = f.read()
f.close

#check whether OverWritten is overwritten
if (OverWritten == 'I wrote this code.') or (OverWritten == 'This code is written by ME.'):
    subprocess.run('color f0 ' #white
                   +'& echo crashed & timeout 5 > nul '
                   +'& color 0f & echo Nice crash!!! '#black
                   +'& timeout 3 > nul', shell=True)
else:
    print(TextContents)
    time.sleep(3)

#Copyright (c) 2024 Gimeitarou
#This software is released under the MIT License, see LICENSE.