import subprocess as subp

from colorama import init, Fore
import pywhatkit as kt
from sender import send

color = init()

def main():

    textFile = 'infoFile.text'
    info = subp.check_output(['systeminfo']).decode('utf-8')
    information = info[0:720]
    network = info[1670: 3579]
    next = False
    with open(textFile, 'w') as f:
        writeInfo = f.write(info)
        if writeInfo:
            while next == False:
                try:
                    sender = input('sender_gmail: ')
                    password = input('password: ')
                    reciver = input('reciver gmail: ')
                    send(info, senderGmail=sender, passwd=password, reciverGmail=reciver) # aqui enviamos la informacion
                    next = True
                except Exception as e:
                    print(e)
                    continue

    if next == True:
        source_path = "test.jpg"
        target_path = 'nft_ascii_art.text'
        art = kt.image_to_ascii_art(source_path, target_path)
        print(Fore.RED + art)

if __name__ == '__main__':
    try:
        main()
    except:
        print('error')