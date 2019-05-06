from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_keys():
	# RSA modulus length must be a multiple of 256 and >= 1024
	modulus_length = 256*4 # use larger value in production
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey

def encrypt_message(a_message , publickey):
	encrypted_msg = publickey.encrypt(a_message, 32)[0]
	encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
	return encoded_encrypted_msg

def decrypt_message(encoded_encrypted_msg, privatekey):
	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
	return decoded_decrypted_msg

########## BEGIN ##########

#a_message = "Hello Nick, I definitely didn't wait until close to last minute to complete these sentences for you. Sorry about that."
#privatekey , publickey = generate_keys()
#pubKeyFromNick = base64.b64decode('MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsOlKAao/vXh2yVYS2RNH+M+Vb/XX6qnqpX9uIuwpqh9gnI6ZjDHv8T6uIJ1BSLuajAuHQTO+7ZFz7lh7cSm/SXdA3RsR1Vwp9k+Jwituuapm52RKhX6Mix8FMhoP+dEBrD4wLJYfX4oAvvg5uqw3F4gja32IjhdNXIZaMwBeJpQIDAQAB')
#publickey = RSA.importKey(pubKeyFromNick)
privKeydecode = base64.b64decode('MIICWwIBAAKBgQCyAdOQJOCCkVr+SLe0jr5FHQKEfP1MXLr/yfKU5iernnIMqtSFajCEVJ1ZtZKKuh0aJrSomh8lcJFII+oKZnk/wVoBSPLg3DvONJMQ2pZLN3vAmtgTPd+S0oj4lnai1A6d4t7IrkOEa9aGthSb5WYlDvbV7ljd9h0/hxbsRsLaRQIDAQABAoGANxatnLxs5ruJR4zFnZFXfRgfQVVVJp7EGIktE7uup0Qf05/CqY9VeH6fO7YfpeM3QnKcElmwLewKaiMDOTjBaN8YQB0oVD97xpXDmDD3alYzAeGfYXEP+FVcv+dPVTmmc49RGUU2q18AiS2V6r3G/JA0CrAOF8ctaoLu3609CUECQQDEEk50Qa8gy2zeZTrJO5yBTsRVnYP6Gf8BSiCIzRXniXHahceZr+YT46n4lmb3dlc3bn5ZHFi2sFCYzV3Fc1YNAkEA6GoQ0mojxksra8+ZxyRD279GE3tl70MZNyRfSPhhhFeQ4rNR7uNU9pVhmSCy2cUpnUL8RiMNJU7fH6WwlUt/GQJAVatWAi/s8BxSHj4G2IQmVs1utaXUU4PmSs7ztjI9vuPsDjnjw3/6vHf9/TLiHH/ljb/GjvL2xCP3ozwgG7TQRQJAU2bsjnWkTN5gwJmJF5t99neXUBpyJAAyJkWZI/huFi3OQmwTNOTDcpF8qpS/WcKVAmgtW4Xsi7zX+OVejtS+0QJAXi1PDX65JV3mEdSf0KZVtdx5G4Tl/M8SKoO2jj7hWhTWOMya6DUujEKX1791Z0JsOLAVJQhW71/5J10ixYvWcg==')
privatekey = RSA.importKey(privKeydecode)
hashFile = open('EncodedMessageForEmily.txt', 'r+')
encrypted_msg = str(hashFile.read())
#encrypted_msg = encrypt_message(a_message , publickey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

#print "%s - (%d)" % (privatekey.exportKey() , len(privatekey.exportKey()))
#print "%s - (%d)" % (publickey.exportKey() , len(publickey.exportKey()))
#print " Original content: %s - (%d)" % (a_message, len(a_message))
print "Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg))
print "Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg))

