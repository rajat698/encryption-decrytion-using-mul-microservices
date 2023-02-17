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