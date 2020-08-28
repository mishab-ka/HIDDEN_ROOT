#!/usr/bin/python
#This Tool Coded BY HIDDEN_RAT



import sys
import os
import time
import banner
import webdir
import admin_panel
import webBro
import ftpcracker
import sshBroute
import subdomine_brote



class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


try:
    I = '\033[1;77m[i] \033[0m'
    Q = '\033[1;77m[?] \033[0m'
    G = '\033[1;34m[*] \033[0m'
    S = '\033[1;32m[+] \033[0m'
    W = '\033[1;33m[!] \033[0m'
    E = '\033[1;31m[-] \033[0m'

    def BruteHelp():
        print('''
HELP
=====

    Command        Description
    -------        -----------
    help           Show help Menu
    use            use a attack (eg: use 1)
    clear          Clear The Screen
    exit           back To main menu
    back           back to attacks
    backk          back To main menu''')

    def BruteMenu():
        print(f'''
        [1] WebPage BrouteForce         [2] SSH BrouteForce
        [3] FTP BrouteForce             [4] SubDomaine Enumation
        [5] Fuzzing                     [6] Cookie BrouteForce
        [7] Admin Pannel Bypass\n
        {Q} \033[1;33mType Help To Show Help Menu \033[0m\n''')
        Brute_menu = input(f'''┌─[root]─[\033[1;32mBrouteForce (Bypass)\033[0m]
└──╼ # ''')
        
        if Brute_menu == "help":
            time.sleep(0.5)
            BruteHelp()
            BruteMenu()  
        elif Brute_menu == "use 1":
            time.sleep(0.5)
            webBro.web_Broute()
            BruteMenu()
        elif Brute_menu == "use 2":
            time.sleep(0.5)
            sshBroute.ssh_cracker()
            BruteMenu()
        elif Brute_menu == "use 3":
            time.sleep(0.5)
            ftpcracker.ftp_crack()
            BruteMenu()
        elif Brute_menu == "use 4":
            time.sleep(0.5)
            subdomine_brote.main1()
            BruteMenu()
        elif Brute_menu == "use 5":
            time.sleep(0.5)
            print("fuzzing..")
            print("Comming Soob....")
            BruteMenu()
        elif Brute_menu == "use 6":
            time.sleep(0.5)
            print("cookie")
            print("Comming Soob....")
            BruteMenu()
        elif Brute_menu == "use 7":
            time.sleep(0.5)
            print("admin bypass")
            print("Comming Soob....")
            BruteMenu()
        elif Brute_menu == "clear":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            BruteMenu()
        elif Brute_menu == "back":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            Attacks_main()
        elif Brute_menu == "backk":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            main_menu()   
        elif Brute_menu == "exit":
            print(f"{W}Exiting...!")
            os.system("exit")
            exit(0)
        else:
            print(f"{E}Invalid Option...")
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            BruteMenu()

    def help1():
        print('''
    Attacks HELP  
    =============

        Command        Description
        -------        -----------
        help           Show help Menu
        use            use a attack (eg: use 1)
        clear          Clear The Screen
        exit           Exit This Tool
        back           back to main menu
        ''')
        
    def Attacks_main():
        print(f'''
        [1] WebSite                   [4] Exploit         
        [2] BrouteForce (Bypass)      [5] Sniffing And Spoofing        
        [3] Hack A Hacker\n
        {Q} \033[1;33mType Help To Show Help Menu \033[0m\n''')
        attacks_menu = input(f'''┌─[root]─[\033[1;32mattacks\033[0m]
└──╼ # ''')
        print(attacks_menu)
        if attacks_menu == "help":
            help1()
            Attacks_main()
        elif attacks_menu == "use 1":
            time.sleep(0.5)
            webSite()
        elif attacks_menu == "use 2":
            BruteMenu()
            time.sleep(0.5)
        elif attacks_menu == "use 3":
            time.sleep(0.5)
            print("Comming Soob....")
            print("Hack A Hacker")
            Attacks_main()
        elif attacks_menu == "use 4":
            time.sleep(0.5)
            print("Comming Soob....")
            print("Exploit")
            Attacks_main()
        elif attacks_menu == "use 5":
            time.sleep(0.5)
            print("Comming Soob....")
            print("sniffing and spoofing")
            Attacks_main()
        elif attacks_menu == "clear":
            os.system("clear")
            print(banner.random_ch)
            Attacks_main()
        elif attacks_menu == "back":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            main_menu()
        elif attacks_menu == "exit":
            print(f"{W}Exiting...!")
            time.sleep(1)
            os.system("exit")
            exit(0)
        else:
            print(f"{E}Invalid Option...")
            time.sleep(2)
            Attacks_main()

    def help():
        print('''
    Core Commands  
    =============

        Command        Description
        -------        -----------
        help           Show help Menu
        \033[32mattacks\033[0m        Show Attacks
        clear          Clear The Screen
        exit           Exit This Tool
        update         Update Tool
        ''')

    hostname = os.uname()[1]

    def main_menu():
        ui = input(f'''┌─[root]─[\033[1;32m{hostname}\033[0m]
└──╼ # ''').strip(" ")

        ui = ui.split()
        if ui == []:
            pass
        elif ui[0] == "help":
            help()
            main_menu()
        elif ui[0] ==  "attacks":
            time.sleep(0.5)
            Attacks_main()
        elif ui[0] == "clear":
            os.system("clear")
            print(banner.random_ch)
            main_menu()
        elif ui[0] == "exit":
            print(W + "Exiting...!")
            time.sleep(0.5)
            os.system("exit")
            exit(0)
        elif ui[0] == "update":
            print(I + "Comming Soon..!")
            time.sleep(1)
            main_menu()
        else:
            print(E + "Invalid Command...")
            time.sleep(0.5)
            main_menu() 

    def webhelp():
        print('''
    HELP
    =====

        Command        Description
        -------        -----------
        help           Show help Menu
        use            use a attack (eg: use 1)
        clear          Clear The Screen
        backk          back To main menu
        back           back to attacks
        exit           exit Tool''')

    def webSite():
        print(f'''
        [1] WebSite Diractory Finder [6] WebPage BrouteForce
        [2] Admin Panel Finder       [7] SubDomaine Enumaration    
        [3] FTP BrouteForce          [8] Cookie BrouteForce
        [4] Fuzzing                  [9] SSH BrouteForce
        [5] Admin Pannel Bypass      
        \n
        {Q} \033[1;33mType Help To Show Help Menu \033[0m\n''')
        web_menu = input(f'''┌─[root]─[\033[1;32mWeb Attacks\033[0m]
└──╼ # ''')
        
        if web_menu == "help":
            webhelp()
            webSite()   
        elif web_menu == "use 1":
            time.sleep(0.5)
            webdir.webDir()
            webSite()
        elif web_menu == "use 2":
            time.sleep(0.5)
            admin_panel.admin_panel_fider()
            webSite()
        elif web_menu == "use 3":
            time.sleep(0.5)
            ftpcracker.ftp_crack()
            webSite()
        elif web_menu == "use 4":
            time.sleep(0.5)
            print("Comming Soob....")
            print("Fuzzzzing...")
            webSite()
        elif web_menu == "use 5":
            time.sleep(0.5)
            print("Comming Soob....")
            print("admin bypass...")
            webSite()
        elif web_menu == "use 6":
            time.sleep(0.5)
            webBro.web_Broute()
            webSite()
        elif web_menu == "use 7":
            time.sleep(0.5)
            subdomine_brote.main1()
            webSite()
        elif web_menu == "use 8":
            print("Coockie BrouteForce...")
            print("Comming Soob....")
            time.sleep(0.5) 
            webSite()
        elif web_menu == "use 9":
            time.sleep(0.5)
            sshBroute.ssh_cracker()
            webSite()
        elif web_menu == "clear":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            webSite()
        elif web_menu == "back":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            Attacks_main()
        elif web_menu == "backk":
            time.sleep(0.5)
            os.system("clear")
            print(banner.random_ch)
            main_menu()   
        elif web_menu == "exit":
            print(f"{W}Exiting...!")
            os.system("exit")
            exit(0)
        else:
            print(f"{E}Invalid Option...")
            time.sleep(0.5)
            webSite()
        
    print(banner.random_ch)
    main_menu()

        
            
except KeyboardInterrupt:
    print("\n" + E + "Ctrl + C Exiting...")
    time.sleep(1)
    
except EOFError:
    print("\n" + E + "Ctrl + D Exiting...")
    time.sleep(1)
    exit(0)


