import sys
input_string, cipher = sys.argv[1:]               #User inputs

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

#Print the output
print(encryption(input_string))