import random
import string
def rand0m1():
    character = string.ascii_lowercase
    return random.choices(character,k=3)
RANDOM1 = ("".join(rand0m1()))

def rand0m2():
    character = string.ascii_lowercase
    return random.choices(character,k=3)
RANDOM2 = ("".join(rand0m2()))

msg = input("Type your message_____")
words = msg.split()
coding = input("1 for Coding or 0 for Decoding___")
coding = True if (coding=="1") else False

if (coding):
    nwords =[]
    a = RANDOM1
    b = RANDOM2
    for word in words:
        if len(word) >=3:
            secret = a + word[1:] + word[0] + b
            nwords.append(secret)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word)>3:
          secret = word[3:-3]
          secret = secret[-1]+ secret[:-1]
          nwords.append(secret)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))