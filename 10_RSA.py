# Emily Clark
# CS 423
# 2-12-19
# CryptoExercise # 10, Make our own key, make it functional..

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
	encrypted_msg = 'rJ3MefoMSYYPu0joJihhGcNPv44WRC7vIYUBg01nqF504UHUemFXqQa2dJYyB7YFEaHdOzy45cfPCpT68zUIl45blza21oOVwY73rFpONpRm+Ucsw5KTMc74yaxmESCF7UmeZDIVfdBO84poZbdezUMVkuItWo4LjY55RKJVJU='
	decoded_encrypted_msg = base64.b64decode(encrypted_msg)
	decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
	return decoded_decrypted_msg

########## BEGIN ##########

#a_message = "This is the last homework assignment, pretty hype."
#privatekey , publickey = generate_keys()
#pubKeyNick = base64.b64decode("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLeq9dDZi//aqHxvyCAtrj7OI/nT4fIyNhA2VXGHa41g4Hh8BoubjZQafgot+g2ZPBjI/8ZJnclloFsig00pRh7u1gDrRtoW9o6WrN1llh+b1JWWADFDmevi4Am8zk1bjzB2K7c+x+olJ3s2dGKWumysVZcdwOucAjJuH5ViPjVQIDAQAB")
#publickey = RSA.importKey(pubKeyNick)
#encrypted_msg = encrypt_message(a_message, publickey)
encrypted_msg = 'rJ3MefoMSYYPu0joJihhGcNPv44WRC7vIYUBg01nqF504UHUemFXqQa2dJYyB7YFEaHdOzy45cfPCpT68zUIl45blza21oOVwY73rFpONpRm+Ucsw5KTMc74yaxmESCF7UmeZDIVfdBO84poZbdezUMVkuItWo4LjY55RKJVJU='
privKey = base64.b64decode("MIICXAIBAAKBgQDLeq9dDZi//aqHxvyCAtrj7OI/nT4fIyNhA2VXGHa41g4Hh8BoubjZQafgot+g2ZPBjI/8ZJnclloFsig00pRh7u1gDrRtoW9o6WrN1llh+b1JWWADFDmevi4Am8zk1bjzB2K7c+x+olJ3s2dGKWumysVZcdwOucAjJuH5ViPjVQIDAQABAoGAJ2y78ZGi2QAzPF+HqUEYXDUXmS/ES5ApWLCpv/hTeHiw+zCITUI+2IlqF5I3NhkyEbxEYai0TxMqmhPsyl9KtF3wBasySxTaa8hhr4D4MV/H/YtnbqNc4thXu7E8gRKhySWUKjvO/QYZaRES9Bu/p6bodRtllHkqFY8G4lC+xrkCQQDL9lWoaA33OcG0OU5XdfldV51t+SaP/cZANsAR/QPVkf6hAyNm9XWyv3c8K0otvk7HhRrNwy6Tuw0w16lHSa9XAkEA/2TNnF6221S6YnHQFbI1r4WzRS17urerEMOZjFkqr18LzI+9yruVoqHlrsGgKEb65kH6a5fZmfkD3+9ughGTMwJAcymnu+rk187YvHYO8fs+zaGG1m1zhKH5qpA/aui9nX1NlIQ9HQlDZ6YMIQEgZSurN6TEOaIXTnqzO/zJK+NDCQJAf/i7ynnvOHH5PvD2qph0rDHbhXNoB0SXNDw+yYO4js2adPMlz9s0/JwRIgMlxGjkudIfsCATykJrvZ8VCZnS3wJBAKmEuN+XkQ2waxSYSyRC2Z+M1AL9LGI9PzOp+9LKPWdf93SgbGauytJPKJ00p3Ve7lhbcsdT2f7cc1ooPM4iS4g=")
privatekey = RSA.importKey(privKey)
decrypted_msg = decrypt_message(encrypted_msg, privatekey)

#print "%s - (%d)" % (privatekey.exportKey() , len(privatekey.exportKey()))
#print "%s - (%d)" % (publickey.exportKey() , len(publickey.exportKey()))
#print " Original content: %s - (%d)" % (a_message, len(a_message))
#print "Encrypted message: %s - (%d)" % (encrypted_msg, len(encrypted_msg))
print "Decrypted message: %s - (%d)" % (decrypted_msg, len(decrypted_msg))

