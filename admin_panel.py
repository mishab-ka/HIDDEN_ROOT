import requests
from termcolor import colored
def admin_panel_fider():

    I = '\033[1;77m[i] \033[0m'
    # Q = '\033[1;77m[?] \033[0m'
    # G = '\033[1;34m[*] \033[0m'
    S = '\033[1;32m[+] \033[0m'
    # W = '\033[1;33m[!] \033[0m'
    E = '\033[1;31m[-] \033[0m'

    session = requests.Session()
    session.max_redirects = 60

    try:
            def request(url):
                try:
                    return requests.get(url, allow_redirects=True)
                except requests.exceptions.ConnectionError:
                    print(colored("[!] Inrenet Error...!", 'red'))
            

            target_url = input(colored("[*] Enter Target URL: ", 'yellow'))
            file1 = input(colored("[*] Enter Wordlist Path: ", 'yellow'))
            file = open(file1, "r")

            for line in file:
                line = line.strip()
                full_url = target_url + "/" + line
                response = request(full_url)
                if response:
                    status_code1 = requests.get(full_url, allow_redirects=True).status_code

                    print(colored("[+] Found: --> " + full_url, 'green'))
                    print("[+] Code: ", status_code1)
    except KeyboardInterrupt:
            print(colored("\n[-] Ctrl + c Detected..!", 'red'))
    except EOFError:
            print(colored("\n[-] Ctrl + D Detected..!", 'red'))
    except FileNotFoundError:
            print(colored("\n[-] File NOT Found..!", 'red'))
    except requests.exceptions.MissingSchema:
            print(colored("\n[-] Url Not Found..! ", 'red'))
            print(colored("\n[i] Not Using 'http://' or 'https://' (Exampul:http://url.com)", 'blue'))
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
