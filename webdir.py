#!/usr/bin/python
def webDir():
    import requests
    from termcolor import colored
    I = '\033[1;77m[i] \033[0m'
    # Q = '\033[1;77m[?] \033[0m'
    G = '\033[1;34m[*] \033[0m'
    S = '\033[1;32m[+] \033[0m'
    W = '\033[1;33m[!] \033[0m'
    E = '\033[1;31m[-] \033[0m'

    try:
        def request(url):
            try:
                return requests.get(url)
            except requests.exceptions.ConnectionError:
                print(colored(W + "Inrenet Error...!", 'red'))
                
        target_url = input(colored(G + "Enter Target URL: ", 'yellow'))
        file1 = input(colored(G + "Enter Wordlist Path: ", 'yellow'))
        file = open(file1, "r")

        for line in file:
            line = line.strip()
            full_url = target_url + "/" + line
            response = request(full_url)
            if response:
                status_code1 = requests.get(full_url).status_code

                print(colored(S + "Found: --> " + full_url, 'green'))
                print(S + "Code: ", status_code1)
            
    except KeyboardInterrupt:
        print(colored("\n[-] Ctrl + c Detected..!", 'red'))
    except EOFError:
        print(colored("\n[-] Ctrl + D Detected..!", 'red'))
    except FileNotFoundError:
        print(colored("\n[-] File NOT Found..!", 'red'))
    except requests.exceptions.MissingSchema:
        print(S + "Mission passed!")
        print(colored("\n[-] Url Not Found..! ", 'red'))
        print(colored(I + "Not Using 'http://' or 'https://' (Exampul:http://url.com)", 'blue'))
        print(colored(I + "or Check URL or Host is Down", 'blue'))
    except requests.exceptions.Timeout:
        print(S + "Mission passed!")
        print(E + "Sorry Time OUT")
        print(I + "Use New Wordlist")
        print(I + "Check Your InterNet Connection...")
    except  requests.exceptions.ConnectionError:
        print(S + "Mission passed!")
        print(E + "Sorry Time OUT")
        print(I + "Use New Wordlist")
        print(I + "Check Your InterNet Connection...")
    except requests.exceptions.TooManyRedirects:
        print(S + "Mission passed!")
        print(E + "Sorry Time OUT")
        print(I + "Use New Wordlist")
        print(I + "Check Your InterNet Connection...")