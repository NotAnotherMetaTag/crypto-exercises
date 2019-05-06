import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]


def iv():
    """
    The initialization vector to use for encryption or decryption.
    It is ignored for MODE_ECB and MODE_CTR.
    """
    return "1234567891234567"


class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """


    def __init__(self, key):
        self.key = key
        #self.key = hashlib.sha256(key.encode()).digest()


    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')


    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


key = 'sixteencharacter'


#message = 'Wut'
#_enc = 'gOXlygE+qxS+69zN5qC6eKJvMiEoDQtdoJb3zjT8f/E='
#message = 'imcore.net'
#enc = 'kWyuTmUELRiREWIPpLy3ZA=='
#message = 'Test English...'
#answer = 'rvs4H8x4Q8sblGG1jkOHFQ=='

hashFile = open('EncryptedForEmily.txt', 'r+')
msg = str(hashFile.read())
#enc = AESCipher(key).encrypt(msg)
dec = AESCipher(key).decrypt(msg)
#print enc
print dec

#print(_enc == enc)
#print(message == dec)
