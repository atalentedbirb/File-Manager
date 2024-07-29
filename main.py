import questionary
import sys
import pyuac, colorama
import animations
import organize, about

selection_list= ['GRANT ADMIN PRIVILEDGES','ORGANIZE', 'HELP', 'EXIT']
print('THIS PROGRAM REQUIRES ADMIN PRIVILEDGES TO RUN!\n')
while 1:
    if not pyuac.isUserAdmin():
        print('Admin priviledges granted: ', colorama.Style.BRIGHT+colorama.Fore.RED+'✗')
        colorama.init(autoreset= True)
    else:
        print('Admin priviledges granted: ', colorama.Style.BRIGHT+colorama.Fore.GREEN+'🗸')
        colorama.init(autoreset= True)
        if selection_list[0] == 'GRANT ADMIN PRIVILEDGES':
            selection_list.pop(0)
    
    choice= questionary.select('FILE ORGANIZER: ', choices=selection_list).ask()

    if choice == 'EXIT':
        x= input("Do you really want to exit?[Y/N]").upper().strip()
        if x == 'Y':
            print('EXITING             ', end= '')
            animations.usethisforspinningcursor(24)
            sys.exit()

    elif choice == 'ORGANIZE':
        file_path=input('Enter the directory you want to organize: ').strip()
        organize.allofcodehere(file_path)
        
    elif choice == 'HELP':
        about.main()
    elif choice == 'GRANT ADMIN PRIVILEDGES':
        pyuac.runAsAdmin()
        

