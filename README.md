# ryadav17_a4_act1

* Command to run encryption container:-
docker run encrypt Rajat Yadav (string: Rajat, cipher: Yadav)

* Command to run decryption container:-
docker run decrypt Rajat Yadav (string: Rajat, cipher: Yadav)

* The two containers are pipe enabled. Example:- 
I tried in powershell: docker run decrypt (docker run encrypt Rajat Yadav) Yadav
This will return original string - "Rajat".