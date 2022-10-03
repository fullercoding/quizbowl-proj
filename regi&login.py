import requests
import base64
import json
url = "https://cae-bootstore.herokuapp.com/"

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_question ="/question"


def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        "Content-Type":"application/json"
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text

def login_user(user_name, password):
    auth_string = user_name + ":" + password
    headers = {
        "Authorization":"Basic " + base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url+endpoint_login,
        headers = headers
    )
    return user_data.json()
    