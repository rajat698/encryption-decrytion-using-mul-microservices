docker image build -t decrypt_socker <path to the conaining folder>
docker run -d -p 5002:5000 decrypt_socket

2. Now you can test using postman, since out local server is hosted.

enter the http URL from flask http://127.0.0.1:5002/
enter 2 arguments:-
1.text (Input string)
2.cipher (Cipher string)

Done!!