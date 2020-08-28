import requests
import time
import urllib3
import sys

vertion = 2.2

I = '\033[1;77m[i] \033[0m'
Q = '\033[1;77m[?] \033[0m'
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
E = '\033[1;31m[-] \033[0m'
# def parse_args():
#     import argparse
#     paser = argparse.ArgumentParser()
#     paser.add_argument('-d', '--domain',  type=str, required=True, help='Target Domin')
#     paser.add_argument('-o', '--output', type=str, required=False, help='Output file')
#     return paser.parse_args()


def main1():


    def parse_url(url):
        try:
            host = urllib3.util.url.parse_url(url).host
        except Exception as e:
            print(E + "invalide Domain")
            sys.exit(0)
        return host

    def file_sub(subdomain, output_file):
        with open(output_file, 'a') as fp:
            fp.write(subdomain + '\n')
            fp.close()

    def main():
        
        subdomains = []
        # args = parse_args()
        tar = input(G + "Enter Target Domain: ")

        target = parse_url(tar)
        output = input(G + "Enter Your OutPut File Name: ")

        req = requests.get(f'https://crt.sh/?q=%.{target}&output=json')

        if req.status_code != 200:
            print(E + "Some Thing is Error")
            sys.exit(0)

        for (key,value) in enumerate(req.json()):
            subdomains.append(value['name_value'])

        print(f"\n[!] TARGET: {target}")

        subs = sorted(set(subdomains))

        for s in subs:
            print(S + f"{s}\n")
            if output is not None:
                file_sub(s, output)
        print(S + "Task Finishd....")
    main()
