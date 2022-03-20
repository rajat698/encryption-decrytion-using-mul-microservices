#Note - Enter [encrypt | decrypt] <string> <cipher> first to run tests as well
import unittest
choice, input_string, cipher = input().split()                  #User inputs

KEY = 0                                                         #Calculating sum of ASCIIs of cipher
for i in range(len(cipher)):
    KEY += ord(cipher[i])

def encryption(text):                                      #Function to encrypt

    new_text = ""
    for i in range(len(text)):
        char = text[i]
        val = (ord(char) + KEY) % 128
        if val < 32:
            val = val + 32
        new_text += chr(val)
    return new_text

def decryption(text):                                      #Function to decrypt

    new_text = ""
    for i in range(len(text)):
        char = text[i]
        val = (ord(char) - KEY) % 128
        if val < 32:
            val = val + 32
        new_text += chr(val)
    return new_text

if choice == 'encrypt':                                             #Main
   print(encryption(input_string))

elif choice == 'decrypt':
    print(decryption(input_string))
else:
    print("Unknown choice")

#Unitests - TDD
class TDD(unittest.TestCase):
    #I have used the Cipher text "Yadav" which makes the KEY = 501

    def test_encrypt(self):
        result = encryption("!!##")
        self.assertEqual(result, "6688")

    def test_decrypt(self):
        result = decryption("~~}")
        self.assertEqual(result, "))(")

if __name__ == '__main__':
    unittest.main()