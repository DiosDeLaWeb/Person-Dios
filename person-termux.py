#team: Skull's Society 404 
 
import os
import sys
import time

#cores1
w = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"

#cores2
Azul = '\033[94m'
Verde = '\033[92m'
Amarelo = '\033[93m'
Vermelho = '\033[91m'
Fim = '\033[0m'

def dios(x):
    w = {'w':90, 'm':31, 'h':32, 'k':33, 'b':34, 'p':35, 'a':96, 's':97}
    for i in w:
        x = x.replace('\r%s'%i, '\033[%s;1m'%w[i])
        x += '\033[0m'
        x = x.replace('\r0','\033[0m')
        print (x)

os.system('pkg install ruby cowsay toilet figlet')
os.system('gem install lolcat')

def runntxt(lolz):
    for noobs in lolz:
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10. / 100)
        
#banner
def banner():
    os.system('clear')
    os.system('cowsay -f eyes "skulls" | lolcat')
    os.system('toilet -f standard "SKULLS" -F gay')
    print "          \033[92mDIOS PERSON SKULLS\033[0m"
    print "+---------------------------------------------+"
    print "| Codder by : \033[92mDios De La Web\033[0m"
    print "| github : \033[92mhttps://www.github.com/DiosDeLaWeb\033[0m" 
    print "| Team : \033[92mSKULL'S SOCIETY 404\033[0m"
    print "| +-----------------------------------------+"
    print "| | \033[92m[\033[0m 1 \033[92m]\033[0m \033[93mTERMUX EDIT PERSON\033[0m                   |"
    print "| | \033[92m[\033[0m 2 \033[92m]\033[0m \033[93mEDITAR NICK\033[0m                          |"
    print "| | \033[92m[\033[0m 3 \033[92m]\033[0m \033[93mINSTALE O PACOTE\033[0m                     |"
    print s+"+---+-----------------------------------------+"
    print m+" [ 4 ].Exit"
def main():
    banner()
    print a+",~~~~~",h+"[",s+"numero:",h+"]"
    dios_person = input("\033[96m'~~~~~> ")
    if dios_person == 1:
        pertama()
        runntxt(w+"...................")
        print " " 
        os.system('cowsay -f eyes "SKULLS" | lolcat')
        os.system('toilet -f standard "SKULLS" -F gay')
        runntxt(h+"     S u c c e s s o...")
        print " "
        runntxt(a+"FAVOR ABRIR UMA NOVA SESSAO NO TERMINAL")
        print " "
        print " "
    elif dios_person == 2:
        print w+'processando.......'
        time.sleep(1)
        noobs()
    elif dios_person == 3:
        install()
    elif dios_person == 4:
        keluar()
    else:
         main()
def pertama():
    os.system('rm $HOME/../usr/etc/bash.bashrc')
    os.system('cp -f bash.bashrc $HOME/../usr/etc')
    os.system('clear')
    print w+ "processando....."
def install():
    os.system('pkg install ruby cowsay toilet figlet')
    os.system('gem install lolcat')
    main()
def keluar():
    sys.exit()

def noobs():
    lol = raw_input('\033[92;1m E D I T A R  A G O R A ?\033[91m[ Y / N ]:')
    if lol == 'y' or lol == 'Y':
        os.system('pkg install nano')
        os.system('nano bash.bashrc')
        main()
    else:
        main()

if __name__ == '__main__':
    main()
