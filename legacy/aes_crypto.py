#!/usr/bin/env python3
import base64

from Crypto.Cipher import AES

''' AES加密解密 支持中文 '''

class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw.encode())
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return decrypted.decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * b'\x00'


if __name__ == '__main__':
    # AES key must be either 16, 24, or 32 bytes long
    key = '1234567890abcdef'
    text = '11aahaa你好aaaaaaaaaaa1b1'

    ac = AESCipher(key)
    mm = ac.encrypt(text)
    print(mm)
    t = ac.decrypt(mm)
    print(t)


