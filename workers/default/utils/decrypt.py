from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random
from app import app
import base64

class Message:
    def __init__(self, message, key_file=app.config['PRIV_KEY']):
        self.key_file = RSA.import_key(open(key_file).read())
        self.message = message

    def decrypt(self):
        decoded_data = base64.b64decode(self.message)        
        cipher_rsa = PKCS1_OAEP.new(self.key_file)
        decrypted_key = cipher_rsa.decrypt(decoded_data[:256])
        iv, value = decoded_data[256:][:16], decoded_data[256:][16:]
        cipher = AES.new(decrypted_key, AES.MODE_CFB, iv, segment_size=128)
        plaintext = cipher.decrypt(value)[:len(value)]
        return plaintext, decrypted_key

    def encrypt(self, key):
        iv = Random.new().read(16)
        cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        message = ('0' * 16) + self.message
        ciphertext = cipher.encrypt(message.encode('utf-8'))
        return ciphertext