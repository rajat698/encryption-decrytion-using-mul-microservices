from urllib import request, parse

url = "http://127.0.0.1:5000/"

data = {'text': '!!##', 'cipher': 'Yadav'}
data = parse.urlencode(data).encode()

req = request.Request(url, data=data, method="POST")
response = request.urlopen(req)

if response.read() == '6688':
    print("Encryption Passed")
elif response.read == 'AACC':
    print("Decryption Passed")