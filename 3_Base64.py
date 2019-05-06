# Emily Clark
# CS 423
# 1-24-19
# CryptoExercise # 3. Base 64 Example

import base64
encoded_data = base64.b64encode(b'Encode this text')
print("Encoded text with base 64 is")
print(encoded_data)

# Decoding base 64:
a = raw_input("Enter encoded text:")
b = base64.b64decode(a)
print b