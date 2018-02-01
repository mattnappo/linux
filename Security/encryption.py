# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64, os
def encryption(privateInfo):
    blockSize = 16
    padding = "{"
    pad = lambda s: s + (blockSize - len(s) % blockSize)
    encodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    keyType = input("Would you like a [R]andomly generated key or [I]nput your own key? ")
    if keyType == "R":
        key = os.urandom(blockSize)
        print("Your key: "+key)
        cipher = AES.new(key)
        encoded = encodeAES(cipher, privateInfo)
        print("Encrypted string: "+encoded)
    elif keyType == "I" or keyType == "i":
        key = input("Enter key: ")
        cipher = AES.new(key)
        encoded = encodeAES(cipher, privateInfo)
        print("Encrypted string: "+encoded)
def decryption(encryptedInfo):
    padding = "{"
    decodeAES = lambda c, e: c.decrypt(base64.b64decode(e).rstrip(padding))
    key = input("Enter key: ")
    cipher = AES.new(key)
    decoded = decodeAES(cipher, encryptedInfo)
    print(decoded)
while True:
    welcome = input("[E]ncrypt, [D]ecrypt, or [Q]uit? ")
    if welcome == "E" or welcome == "e":
        text = input("Enter plain text: ")
        encryption(text)
    elif welcome == "D" or welcome == "d":
        text = input("Enter encrypted text: ")
        decryption(text)
    elif welcome == "Q" or welcome == "q":
        break
