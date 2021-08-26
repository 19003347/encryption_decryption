import random

old=list(map(chr,range(97,123)))

oldupdate=''.join(old)
print(oldupdate)

random.shuffle(old)

newupdate=''.join(old)
print(newupdate)

def encrypt(data):
    store=data.maketrans(oldupdate,newupdate)  # update the values a:j,b:n
    return data.translate(store)    #completely changed

def decrypt(data):
    store=data.maketrans(newupdate,oldupdate)
    return data.translate(store)


source=input("Enter the data : ")
encryption=encrypt(source)
print("Encryption : ",encryption)

decryption=decrypt(encryption)
print("Decryption : ",decryption)





