import threading
import requests
import time

print("  ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ███▄ ▄███▓ ▓█████ ██▀███  ")
print("▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ▓█   ▀▓██ ▒ ██▒")
print("░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▓██    ▓██░ ▒███  ▓██ ░▄█ ▒ ")
print("  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ▒██    ▒██  ▒▓█  ▄▒██▀▀█▄  ")
print("▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒▒██▒   ░██▒▒░▒████░██▓ ▒██▒ ")
print("▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░   ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░")
print("░ ░▒  ░ ░░▒ ░     ░ ░   ▒▒ ░  ░      ░░  ░      ░░ ░ ░    ░▒ ░ ▒ ")
print("░  ░  ░  ░░         ░   ▒  ░      ░   ░      ░       ░    ░░   ░ ")
print("      ░                 ░         ░          ░   ░   ░     ░     ")


print("                                     ")
channel = input('id of channel: ')
mess = input('message to spam: ')
delay = input('delay (s): ')

tokens = open("tokens.txt", "r").read().splitlines()


def spam(token, channel, mess):
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header = {"authorization": token}

    while True:
        time.sleep(int(delay))
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)



def thread():
    channel_id = channel
    text = mess
    for token in tokens:
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()


start = input('press enter ')
start = thread()
