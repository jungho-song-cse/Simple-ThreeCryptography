import matplotlib.pyplot as pp
import numpy as np


message = 'OVSAOXQYVAMFKDNTFHWZKKWQLFCHHDMXGHVRXEICQQCZKKBZESGCKSSTFUKBXVAZXKWFJGUWWHWGHWIYVWBZEZWFJCTQGJSYWGGFNWQDKHOAJAVRJWUUZAVQJCBGUXUPKDSNQAVROCFQYGNHAGRBSDMEAHPRRWBTLPSYKLQETSZRZABMWZSGOLJPOVWFVWZHGFRFUXETKRCZRWBTLPSNTVESWBHUKTZZCSBUKSZEWRDRUHTPDWJVTYQYLVSJUJTOSUFRKLPPJSKVRDJPSBOAYOMCDSHVZTMQGFHUUMOSLVSLSSGMWDOEZWLEZSFROKAEAZZNIZIYUSHUGLBSWMKVRDAPWHVRXWETDZPRGFIYKKSERWBTLPSYKLQETSZRZABMWZSGOLJPDSHVZTMJWOVGNWZPOWZYHWIYSBGJKJTPLWHOKDMEAHPRRWBTLPSYKLQETSZRZABMWKVVYHMCOCFQYGNHAGRBSDMEAHPRRWBTLPSYKLQETSZRZABMWMSNNDMEAHPRCZQDHSFJUJLDGTKVYVWXDSHVZTMLFRKUKFBSWBWTNLQDUZCHJQBSWFSVYKBTDZOYOYPELVOGYZQYWGCASWASABSHTLQWLCABXJWHDSHVZTMTOOYRAHBZLVSFUMVOGTAHYAKXGHVRXEICQQCZKKBZESGCKSSTFUKBXVAZXKWFJGUWWHWGHWTPLWHOKDMEAHPRRWBTLPSLKSPWWHWGHWBSWFSJODTMWOBNTKEPJZSGOLJPDSHVZTMWWHWGHWTPLWHOKQMLZZSGOLJPLVSEKOQWDPSNTSVDOSFYKLQETSZRZABMWZSGOLJPDSHVZTMJWOVYKLQETSKUOKXPJKCEJKWQOWGQUETPLWHOK'
ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#find coincidences by below code
for shift in range(len(message)):
    count = 0
    for i in range(len(message)):
        if(i+1+shift >=len(message)):
            break
        if(message[i]==message[i+1+shift]):
            count += 1
    print(count)
#we found out its key length is 8 by coincidences, so it may be vigenere cipher


#find frequency by below code
letterFrequency = [[0 for a in range(len(ALPHABETS))] for b in range(8)]

for i in range(len(message)):
    letterFrequency[i%8][ALPHABETS.find(message[i])] += 1
for i in range(len(letterFrequency)):
    x = np.arange(26)
    axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pp.bar(x, letterFrequency[i])
    pp.xticks(x, axis)

    pp.show()

#by analyze letterFrequency, I could found the key is 'SOONGXIL' -> SOONGSIL
key = "SOONGSIL"

decryptedMessage = ""
keyCount = 0
for letter in message:
    num1 = ALPHABETS.find(key[keyCount%len(key)])
    num2 = ALPHABETS.find(letter)
    decryptedMessage = decryptedMessage + ALPHABETS[(num2-num1)%len(ALPHABETS)]
    keyCount+=1

print("decryptedMessage: %s" %(decryptedMessage))
print("key: %s" %(key))

