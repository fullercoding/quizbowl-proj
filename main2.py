import requests
import base64
import json
from IPython.display import Image, display, clear_output
import time
import os

url = "https://cae-bootstore.herokuapp.com/"

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_question ="/question/all"


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
    os.system('cls')
    while True:
        questions = requests.get(url+endpoint_question)
        question_number = 0
        for question in questions.json()['questions']:
            print(f'Question #{question_number+1}')
            print(f"Question ID: {question['id']}")
            print(f"Question: {question['question']}")
            print(f"Answer: {question['answer']}\n")
            question_number += 1
        answer = input("Quit to quit: ")
        if answer.lower().strip() == 'quit':
            break
        else:
            print("Invalid input, please try again")

def make_question(token):
    question = input("Submit question: ")
    answer = input("Answer: ")
    admin_ques = {
        "question": question,
        "answer": answer
    }
    payload_json_make = json.dumps(admin_ques)
    #COME BACK TO                          <<<<<<<<---=====-------------------------------------------------------------
    response = requests.post(             #<<<<<----------------========================================================
        url + endpoint_question,
        data = payload_json_make,
        #headers = headers
    )

    if response.ok:
        print("Question submitted")
    else: 
        print("Submit error. retry, admin")

def delete_question():
#Uses token needs <id> of question   #See github  
    pass

# Will be a put request, uses token, needs <id> payload needed with dict answer #See github
# similar to admin_ques = {
#        "question": question,
#        "answer": answer
#    }

#def edit_questions(token, payload):
    #payload_json_string = json.dumps(payload)
    #headers={
        #"Content-Type":"application/json",
        #"Authorization":'Bearer ' + token
    #}
    #response = requests.put(
        #url + endpoint_user,
        #data = payload_json_string,
        #headers = headers
    #)
    #return response.text

#jims_edit_payload={
    #"first_name":"Bill"
#}

#edit_user(jim['token'],jims_edit_payload)
#pass

def start_quizbowl():
    total_correct = 0
    question_number = 0
    while question_number < 2:
        os.system('cls')
        questions = requests.get(url+endpoint_question)
        print(questions.json()['questions'][question_number]["question"])
        answer = input("Enter your answer: ")
        if answer.lower().strip() == questions.json()['questions'][question_number]["answer"]:
            total_correct += 1
            os.system('cls')
            print("That answer is correct! Congrats!")
            time.sleep(2)
        else:
            os.system('cls')
            print("Not even close, try again!")
            time.sleep(2)
        question_number += 1
    os.system('cls')
    print(f"The quiz is now complete, your total is {total_correct} out of 10")
    time.sleep(2)
    


def main():
    while True:
        os.system('cls')
        print("Welcome To the quizbowl!")
        email = input("Type your email to login or Type `register` to Register: ")
        if email.lower().strip() == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                time.sleep(2)
                os.system('cls')
                continue
        elif email.lower().strip() == 'quit':
            os.system('cls')
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
        
            duty = input("Select your duty, 1-5: ")
            if duty == "1":
                os.system('cls')
                view_created()
                time.sleep(1)
                break
            elif duty == "2":
                os.system('cls')
                make_question()
            elif duty == "3":
                os.system('cls')
                delete_question()
                break
            elif duty == "4":
                os.system('cls')
                #edit_questions()
            elif duty == "5":
                os.system('cls')
                start_quizbowl() #shared function for user and admin!
            else:
                print("Invalid Selection")
                time.sleep(2)
                continue
        
        else:
            print("Welcome User")
            answer = input("Would you like to start the quiz or quit? 'start to start' or 'quit to quit': ")
            if answer.lower().strip() == "quit":
                break
            elif answer.lower().strip() == "start":
                start_quizbowl() #shared function for user and admin!











main()