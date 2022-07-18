import string
import random


s1=list(string.digits)
s2=list(string.punctuation)
s3=list(string.ascii_uppercase)
s4=list(string.ascii_lowercase)

characters_number=input("how many characters for the password:")
while True:
    try:
        characters_number=int(characters_number)
        if characters_number < 6:
            print("your need at least 6 characters")
            characters_number = input("please entre the numbre again :")
        else:
             break
    except:
        print("please entre numbre")
        characters_number = input("how many characters for the password:")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s3)
parte1=round(characters_number*(30/100))
parte2=round(characters_number*(20/100))

password=[]

for i in range(parte1):
    password.append(s3[i])
    password.append(s4[i])
for i in range(parte2):
    password.append(s1[i])
    password.append(s2[i])


random.shuffle(password)
password="".join(password[0: ])
print(password)