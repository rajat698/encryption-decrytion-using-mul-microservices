* Command to run decryption container:-
docker image build -t decrypt <path to the conaining folder>
docker run decrypt Rajat Yadav (string: Rajat, cipher: Yadav)

* The two containers are pipe enabled. Example:- 
I tried in powershell: docker run decrypt (docker run encrypt Rajat Yadav) Yadav
This will return original string - "Rajat".