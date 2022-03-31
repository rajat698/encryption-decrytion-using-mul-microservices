from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])

def encrypt():
    data = request.form
    text = data['text']
    cipher = data['cipher']

    KEY = 0                                                         #Calculating sum of ASCIIs of cipher
    for i in range(len(cipher)):
        KEY += ord(cipher[i])

    new_text = ""
    for i in range(len(text)):
        char = text[i]
        val = (ord(char) - KEY) % 128
        if val < 32:
            val = val + 32
        new_text += chr(val)
    return new_text


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)