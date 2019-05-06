# Emily Clark
# CS 423
# 1-21-19
# CryptoExercise # 2. Hardcode a key = 13 shift.

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# this is only legal alphabet

str_in = raw_input("Enter message, like HELLO: ")
shift = 13
print("Value will be shifted 13")

n = len(str_in)
str_out = ""
str_out2 = ""

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    newloc = ((loc + shift) % 26)
    str_out += alpha[newloc]

print "Encrypted:", str_out

for i in range(n):
    c = str_out[i]
    loc = alpha.find(c)
    newloc = ((loc + shift) % 26)
    str_out2 += alpha[newloc]

print "Decrypted Again:", str_out2
