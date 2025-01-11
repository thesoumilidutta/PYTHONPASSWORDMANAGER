#__main__ 

from colorama import Fore, Style, init
from pickle import dump,load
from cipher import encrypt,decrypt

init(autoreset=True)

def signUp():               #Creates a new account of a user
    name=input(Fore.BLUE+"Enter name : ")
    mobile=int(input(Fore.BLUE+"Enter mobile number : "))
    username=input(Fore.BLUE+"Enter username : ")
    masterkey=input(Fore.BLUE+"Enter Masterkey: ")
    fileobj=open("PASSWORDMANAGER/ENC/logindata.bin","ab")
    dump({(username,mobile,name):masterkey},fileobj)
    fileobj.close()
    fileobj1=open(f"PASSWORDMANAGER/ENC/{username}.bin","wb")
    fileobj1.close()
    return username

def logIn():                #Signs in an existing user
    username=input(Fore.BLUE+"Enter username : ")
    mobile=int(input(Fore.BLUE+"Enter mobile number : "))
    masterkey=input(Fore.BLUE+"Enter masterkey : ")

    fileobj2=open("PASSWORDMANAGER/ENC/logindata.bin","rb")
    c=0
    try:
        while True:
            st=load(fileobj2)
            
            for i in st:                
                if i[0]==username and i[1]==mobile:
                    if st[i]==masterkey:
                        c=1
                        break
            if c==1:
                break
        if (c==1):
            print(Fore.LIGHTMAGENTA_EX+"You have been successfully logged in !")
        else:
            print(Fore.LIGHTMAGENTA_EX+"Yooo the fuck check your username/masterkey before loggin in bro !?")
                
                
    except EOFError:
        fileobj2.close()
    return username

def addingPassword():
    password=input(Fore.LIGHTWHITE_EX+"Enter the password you want to add : ")
    fileobj=open(f"PASSWORDMANAGER/ENC/{username}.bin","ab")
    encryptedPass=encrypt(password)
    dump(encryptedPass,fileobj)
    print(Fore.LIGHTYELLOW_EX+"Password successfully added !")
    
def accessingPassword():
    fileobj=open(f"PASSWORDMANAGER/ENC/{username}.bin","rb")
    try:
        while True:
            st=load(fileobj)                      
            decryptedPass=decrypt(st)
            print(decryptedPass)
    except EOFError:
        fileobj.close()

def deletingPassword():
    passToDelete=input("Enter the pass you want to delete: ")
    passEncrypted=encrypt(passToDelete)
    fileobj=open(f"PASSWORDMANAGER/ENC/{username}.bin","rb")
    topList=[]
    try:
        while True:
            st=load(fileobj)
            if st!=passEncrypted:
                topList.append(st)
            
    except EOFError:
        print("Password successfully deleted !!")
        fileobj.close()
    fileobj1=open(f"PASSWORDMANAGER/ENC/{username}.bin","wb")
    for i in topList:
        dump(i,fileobj1)
    fileobj1.close()

   
#__main__ continuation

print(Style.BRIGHT+Fore.CYAN+"Welcome to password manager")

success=False
response=""
while response!='S' and response!='L':
    response=input(Fore.LIGHTRED_EX+"For signing up enter (S) and for logging in enter (L) :").upper()

if response=='S':
    username=signUp()
    success=True
else:
    username=logIn()
    success=True

while response!="1" and response!="2" and response!="3":
    response=input(Fore.LIGHTYELLOW_EX+"Enter (1) for adding password,\n enter (2) for accessing password and \n enter (3) for deleting password")
if success:
    if response=="1":
        addingPassword()
    elif response=="2":
        accessingPassword()
    else:
        deletingPassword()
