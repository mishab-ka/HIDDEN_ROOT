
import webdir
import banner
import os
import sys

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
    print('''
    [1] WebPage BrouteForce         [2] SSH BrouteForce
    [3] FTP BrouteForce             [4] SubDomaine BrouteForce
    [5] Fuzzing                     [6] Cookie BrouteForce
    [7] Admin Pannel Bypass\n
    {Q} \033[1;33mType Help To Show Help Menu \033[0m\n''')
    web_menu = input(f'''┌─[root]─[\033[1;32mWeb Attacks\033[0m]
└──╼ # ''')
    
    if web_menu == "help":
        BruteHelp()
        BruteMenu()  
    elif web_menu == "use 1":
        print("Web")
        BruteMenu()
    elif web_menu == "use 2":
        print("SSH")
        BruteMenu()
    elif web_menu == "use 3":
        print("FTP")
        BruteMenu()
    elif web_menu == "use 4":
        print("subdomine")
        BruteMenu()
    elif web_menu == "use 5":
        print("fuzzing..")
        BruteMenu()
    elif web_menu == "use 6":
        print("cookie")
        BruteMenu()
    elif web_menu == "use 7":
        print("admin bypass")
        BruteMenu()
    elif web_menu == "clear":
        os.system("clear")
        print(banner.random_ch)
        BruteMenu()
    elif web_menu == "back":
        os.system("clear")
        print(banner.random_ch)
        Attacks_main()
    elif web_menu == "backk":
        os.system("clear")
        print(banner.random_ch)
        main_menu()   
    elif web_menu == "exit":
        print(f"{W}Exiting...!")
        os.system("exit")
        exit(0)
    else:
        print(f"{E}Invalid Option...")
        BruteMenu()
        




        


    
    
