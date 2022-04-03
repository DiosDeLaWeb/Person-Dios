import os
import sys
import time

#colors
w = "\033[90;1m"
m = "\033[91;1m"
h = "\033[92;1m"
k = "\033[93;1m"
b = "\033[94;1m"
p = "\033[95;1m"
a = "\033[96;1m"
s = "\033[97;1m"

def dios(x):
    w = {'w':90, 'm':31, 'h':32, 'k':33, 'b':34, 'p':35, 'a':96, 's':97}
    for i in w:
        x = x.replace('\r%s'%i, '\033[%s;1m'%w[i])
        x += '\033[0m'
        x = x.replace('\r0','\033[0m')
        print (x)

#os.system('pkg install ruby cowsay toilet figlet')
#os.system('gem install lolcat')

def runntxt(lolz):
    for noobs in lolz:
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10. / 100)
        
#banner
def banner():
    os.system('clear')
    os.system('cowsay -f eyes "DIOS" | lolcat')
    dios("\rp          DIOS PERSON SKULLS")
    print s+"+---------------------------------------------+"
    dios ("\ra| Codder by :\rh Dios De La Web")
    dios ("\ra| github :\rh https://www.github.com/DiosDeLaWeb") 
    dios ("\ra| Team :\rh SKULL'S SOCIETY 404")
    print s+"| +-----------------------------------------+"
    dios("\rm| | \rm[\rs1\rm]\rk TERMUX EDIT PERSON          |")
    dios("\rm| | \rm[\rs2\rm]\rk COMO EDITAR                      |")
    dios("\rm| | \rm[\rs3\rm]\rh Instale o pacote primeiro....      |")
    print s+"+---+-----------------------------------------+"
    print m+" 4.Exit"
def main():
    banner()
    print a+",~~~~~",h+"[",s+"numero:",h+"]"
    dios_person = input("\033[96m'~~~~~> ")
    if dios_person == 1:
        pertama()
        runntxt(w+"...................")
        print " " 
        os.system('cowsay -f eyes "SKULLS" | lolcat')
        os.system('toilet-f standard "SKULLS" -F gay')
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
    print '''
COMO EDITAR A SCRIPT BASH.BASHRC

a string que diz
SKULLS com seu nome
ou em qualquer outra palavra que você quer
não altere strings que não sejam "SKULLS",
preocupado que o programa se torne um erro...
caso tenha sido editado, basta salvar pressionando
CTRL + X + Y  + ENTER .
     Codder by : Dios De La Web
     team : SkullS Society 404
 '''
    lol = raw_input('\033[92;1m E D I T A R  A G O R A ?\033[91m[ Y / N ]:')
    if lol == 'y' or lol == 'Y':
        os.system('pkg install nano')
        os.system('nano bash.bashrc')
        main()
    else:
        main()

if __name__ == '__main__':
    main()
