import os
import getch
import animations
import shutil
import sys
import killswitch
import time
import threading


def allofcodehere(filepath):
    boo= True
    def loadingbecausethreadingdidntworkasintended():
        print('LOADING                         /', end= '')
        while boo:
            if not boo:
                break
            for cursor in '\\|/-':
                time.sleep(0.1)
                print(f"\b{cursor}", end= '', flush=True)
    
    if killswitch.no_no_folder_windows(filepath):
        print('That\'s the root folder, exiting program immediately')
        animations.spinning_cursor_new(20)
        sys.exit()
    try:
        while 1: #forever loop until broken by if or else
            if not os.path.exists(filepath):
                print('Path does not exist, try again')
                print('Press any key to go back to menu')
                key= getch.getch()
                if key:
                    break
            else:
                confirm= input('Do you want to continue? [Y/N]').upper().strip()
                if confirm =='N':
                    print('Going back to menu')
                    break
                
                boo= True #starting the animation simultaneously
                loadingobject= threading.Thread(target=loadingbecausethreadingdidntworkasintended)
                loadingobject.start()
                
                os.chdir(filepath) #changes to this filepath
                print('Working on: ', os.getcwd())
                if not os.path.exists('Pictures'):
                    os.mkdir('Pictures')
                if not os.path.exists('Music'): 
                    music_format= ['Lossless', 'MP3']
                    for i in music_format:
                        if not os.path.exists(f'Music\\{i}'):
                            os.makedirs(os.path.join('Music', i), exist_ok=True)
                if not os.path.exists('Text'):
                    os.mkdir('Text')
                 #confirmation #loading 
                
                
                #Organizing
                
                for item in os.listdir(os.chdir(filepath)):
                    if item.endswith('.mp3'):
                        shutil.move(os.path.join(filepath, item), os.path.join('Music/MP3', item))
                    elif item.endswith('.flac'):
                        shutil.move(os.path.join(filepath, item), os.path.join('Music/Lossless', item))
                    elif item.endswith('.txt'):
                        shutil.move(os.path.join(filepath, item), os.path.join('Text File', item))
                    
                print('\nFinished.')
                
                boo= False
                break
    except IOError:
        print('Path could not be deciphered, try again.')
    except ValueError:
        print('It should be a string, try again.')
    
    time.sleep(1)
    boo= False
    loadingobject.join()
    print('\n')