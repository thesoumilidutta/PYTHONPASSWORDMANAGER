def encrypt(passWd):        #Encryption of the password after hashing
    dictForAscii={'0':"agh#",'1':"keyz",'2':"srpp",'3':"wyd?",'4':"felp",
                  '5':"bqsp",'6':"urit",'7':"miwe",'8':"ocxn",'9':"uzjo"}

    hashed=""
    encryptedStr=""
    toAscii=0
    leftPointer,rightPointer=0,len(passWd)-1
    while leftPointer<rightPointer:
        hashed=hashed+passWd[rightPointer]+passWd[leftPointer]
        leftPointer+=1
        rightPointer-=1
    if len(passWd)%2!=0:
        hashed=hashed+passWd[rightPointer]
    
    
    for i in hashed:
        if ord(i)>100:
            toAscii=toAscii*1000+ord(i)
        else:
            toAscii=toAscii*100+ord(i)
    
    for i in str(toAscii):
        encryptedStr+=dictForAscii[i]
    
    return encryptedStr

def decrypt(passWd):            #Decryption of the password after hashing
    dictForAscii={"agh#":'0',"keyz":'1',"srpp":'2',"wyd?":'3',"felp":'4',
                  "bqsp":'5',"urit":'6',"miwe":'7',"ocxn":'8',"uzjo":'9'}
    word=""
    hashed=""
    while len(passWd)>0:
        word=passWd[0:4]
        passWd=passWd[4:len(passWd)]
        hashed+=dictForAscii[word]

    semifinalPass=""
    lis=[]
    finallis=[]
    finalPass=""

    while len(hashed)>0:
        word1=hashed[0:2]

        if int(word1)<65:
            num=int(hashed[0:3])
            hashed=hashed[3:len(hashed)]          
            semifinalPass+=chr(num)
        else:
            num=int(word1)
            hashed=hashed[2:len(hashed)]           
            semifinalPass+=chr(num)

    lis=list(semifinalPass)
   
    for i in range(1,len(lis),2):
        j=lis[i]
        finallis.append(j)
    if len(lis)%2!=0:
        for i in range(len(lis)-1,-1,-2):
            j=lis[i]
            finallis.append(j)
    else:
        for i in range(len(lis)-2,-1,-2):
            j=lis[i]
            finallis.append(j)
      
    finalPass=''.join(finallis)
    
    return finalPass



