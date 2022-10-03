import requests
import base64
import json
from IPython.display import Image, display, clear_output
import time

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


def register():
    clear_output()
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = input("Password: ")
    
    user_dict={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }

    return register_user(user_dict)


def login(email):
    clear_output()
    password = input("Password: ")
    user = login_user(email, password)
    return user

def view_created():
#Will use token, and return dict #See github
    pass

def make_question():
    question = input("Submit question: ")
    answer = input("Answer: ")
    admin_ques = {
        "question": question,
        "answer": answer
    }
    payload_json_make = json.dump(admin_ques)
    #COME BACK TO                          <<<<<<<<---=====-------------------------------------------------------------
    response = requests.post(             #<<<<<----------------========================================================
        url + endpoint_question
        data = payload_json_make
        headers = headers
    )

    if response.ok:
        print("Question submitted")
    else: 
        print("Submit error, retry, admin")

def delete_question():
#Uses token needs <id> of question   #See github  
    pass
def edit_questions():
# Will be a put request, uses token, needs <id> payload needed with dict answer #See github
# similar to admin_ques = {
#        "question": question,
#        "answer": answer
#    }
    pass
def start_quizbowl():
#Will utalize token and end point /question/all #See github
    pass

def main():
    while True:
        clear_output()
        print("Welcome To the quizbowl!")
        email = input("Type your email to login or Type `register` to Register: ")
        if email.lower().strip() == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                time.sleep(2)
                continue
        elif email.lower().strip() == 'quit':
            print("Goodbye")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password Combo")
                time.sleep(2)
                continue
        if email == "connorjfuller@gmail.com":
            print("Welcome admin")
            print("""
Admin duties:
1. View questions submitted
2. Create new question(s)
3. Delete question
4. Edit questions
5. Start quizbowl
             """)
        
            duty = input("Select your duty, 1-4: ")
            if duty == "1":
                clear_output()
                view_created()
                time.sleep(1)
                break
            elif duty == "2":
                clear_output()
                make_question()
            elif duty == "3":
                clear_output()
                delete_question()
                break
            elif duty == "4":
                clear_output()
                edit_questions()
            elif duty == "5":
                clear_output()
                start_quizbowl() #shared function for user and admin!
            else:
                print("Invalid Selection")
                time.sleep(2)
                continue
        
        else:
            print("Welcome User")
            user_response = input("Press ENTER to start quiz bowl!!!")
            if user_response.lower() == "enter":
                start_quizbowl() #shared function for user and admin!
            pass











main()