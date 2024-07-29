from datetime import datetime
import shutil
import colorama

def center_text(text):
        terminal_width = shutil.get_terminal_size().columns
        text_width = len(text)
        left_padding = (terminal_width - text_width) // 2
        centered_text = ' ' * left_padding + text
        return centered_text
    
def main():
    colorama.just_fix_windows_console()

    #dev console
    support= 5
    filesupportlist= ['MP3, FLAC, TXT, PNG, JPEG, JPG']
    #end

    

    print(center_text('FILE MANAGER v1.0.0'))
    print('\n')
    timestamp= str(datetime.now())
    print(center_text('Current Timestamp: '+ timestamp))
    print('\n')

    print(center_text(colorama.Fore.WHITE+f'This is a file manager, it classifies your file into {support} categories:'))
    for i in filesupportlist:
        print(center_text(f'- {i}'))

    colorama.init(autoreset= True)
    print('\n')
    print(center_text(colorama.Style.BRIGHT+colorama.Fore.RED+'WARNING: DO NOT USE IT IN WINDOWS DIRECTORY (WHERE THE OS IS INSTALLED). YOU WILL BE HELD LIABLE FOR ANY LOSS DUE TO IT.'))
    print('\n')
    print(center_text('Directions to use:'))
    print(center_text('1>Copy path of the directory you want to organize (i.e Folder with its whole path, not any file)'))
    print(center_text('2>Navigate to Organize menu and paste the file path as instructed.'))
    print(center_text('3>Profit'))

    print('\n')
    print(center_text('Socials: Check my github profile @atalentedbirb'))
    print(center_text('Made in Atlanta, GA. Made by atalentedbirb. License: MIT License'))

main()