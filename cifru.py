import encryption

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import os
from Cryptodome.Random import get_random_bytes

class cifru1(encryption.login_password):
    
    def encrypt(self, password, N):
        salt = get_random_bytes(AES.block_size)

        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=N, r=8, p=1, dklen=32)

        cipher_config = AES.new(private_key, AES.MODE_GCM)
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(password, 'utf-8'))

        return {
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
            }
    
    def decrypt(self, enc_dict, password, N):
        cipher_text = b64decode(enc_dict['cipher_text'])
        nonce = b64decode(enc_dict['nonce'])
        tag = b64decode(enc_dict['tag'])
        salt = b64decode(enc_dict['salt'])
    
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=N, r=8, p=1, dklen=32)

        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted
