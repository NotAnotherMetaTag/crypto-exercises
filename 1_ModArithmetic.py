# Emily Clark
# CS 423
# 1-21-19
# CryptoExercise # 1. Replace with modulo.

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# this is only legal alphabet

str_in = raw_input("Enter message, like HELLO: ")
shift = int(raw_input("Shift value, like 3: "))

n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    newloc = ((loc + shift) % 26)
    str_out += alpha[newloc]

print "Obfuscated version:", str_out

# Using the mod function resolves the issue of getting non-alphabet characters from ASCII encoding
# Reduces amount of code necessary for error handling.
