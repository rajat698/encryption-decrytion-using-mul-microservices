# ryadav17_a4_act1

* Command to run encryption container:-
docker image build -t encrypt <path to the conaining folder>
docker run encrypt Rajat Yadav (string: Rajat, cipher: Yadav)

* Command to run decryption container:-
docker image build -t decrypt <path to the conaining folder>
docker run decrypt Rajat Yadav (string: Rajat, cipher: Yadav)

* The two containers are pipe enabled. Example:- 
I tried in powershell: docker run decrypt (docker run encrypt Rajat Yadav) Yadav
This will return original string - "Rajat".

# Socket enabled Images:-

* Commads for encryptions and testing
1. I built using flask for python using HTTP

docker image build -t encrypt_socker <path to the conaining folder>
docker run -d -p 5001:5000 encrypt_socket

2. Now you can test using postman, since out local server is hosted.

enter the http URL from flask http://127.0.0.1:5001/
enter 2 arguments:-
1.text (Input string)
2.cipher (Cipher string)

Done!!

* Commads for decryptions and testing

docker image build -t decrypt_socker <path to the conaining folder>
docker run -d -p 5002:5000 decrypt_socket

2. Now you can test using postman, since out local server is hosted.

enter the http URL from flask http://127.0.0.1:5002/
enter 2 arguments:-
1.text (Input string)
2.cipher (Cipher string)

Done!!

# TDD - Docker compose

1. cd to the root directory.
2. Run command - docker-compose up -d
Now all the 3 comtainers are running in detatched mode

Go to postman and give Input string as "!!##".
You will get the testing results now!!