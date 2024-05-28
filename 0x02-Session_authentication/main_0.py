#!/usr/bin/python3
""" Check response
"""
import requests
import base64

if __name__ == "__main__":
    user_email = "u3@hbtn.io"
    user_clear_pwd = "pwd"
   
    basic_clear = "{}:{}".format(user_email, user_clear_pwd)
    r = requests.get('http://127.0.0.1:3456/api/v1/users', headers={ 'Authorization': "Basic {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")) })
    if r.status_code != 200:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    if r.headers.get('content-type') != "application/json":
        print("Wrong content type: {}".format(r.headers.get('content-type')))
        exit(1)
    
    try:
        r_json = r.json()
        
        if len(r_json) == 0:
            print("/api/v1/users should not be empty")
            exit(1)
        
        user_found = False
        for u_j in r_json:
            u_j_email = u_j.get('email')
            if u_j_email is None:
                continue
            if u_j_email == user_email:
                user_found = True
                break
            
        if not user_found:
            print("/api/v1/users should return the user who requested this resource")
            exit(1)

        print("OK", end="")
    except:
        print("Error, not a JSON")