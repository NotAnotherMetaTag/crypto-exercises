# Emily Clark
# CS 423
# 2-12-19
# CryptoExercise # 6, Use a hash and salt and compare to the list of passwords provided.

from passlib.hash import sha512_crypt

hashFile = open('resources/Linux passwords.txt', 'r+')
hashArray = hashFile.readlines()
hashDict = {}
saltArray = []

for hash in hashArray:
    if hash.strip():
        tempStr = str(hash)[:-21]
        key, value = tempStr.split(':', 1)
        hashDict[key] = value
        salt = str(hashDict[key])[3:11]
        saltArray.append(salt)

for c1 in range(20):
    if c1 < 10:
        p = '0' + str(c1)
    else:
        p = str(c1)

    for one in range(5):
        saltHash = (sha512_crypt.using(salt=saltArray[one], rounds=5000).hash("secure" + p))
        if saltHash in hashDict.values():
            print (p, (list(hashDict.keys())[list(hashDict.values()).index(saltHash)]), saltHash)