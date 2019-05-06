# Emily Clark
# CS 423
# 2-12-19
# CryptoExercise # 5, Use a hash and compare to the list of passwords provided.

import hashlib

hashFile = open('resources/Microsoft accounts.txt', 'r+')
hashArray = hashFile.readlines()
hashDict = {}
for hash in hashArray:
    if hash.strip():
        tempStr = str(hash)[:-5]
        tempStr = tempStr.lower()
        key, mid, value = tempStr.split(':', 2)
        hashDict[key] = value

for c1 in range(100):
    if c1 < 10:
        p = '0' + str(c1)
    else:
        p = str(c1)

    hash = hashlib.new("md4", p.encode("utf-16le")).hexdigest()
    if hash in hashDict.values():
        print p, (list(hashDict.keys())[list(hashDict.values()).index(hash)]), hash
