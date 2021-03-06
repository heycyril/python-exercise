"""
import json

def greet_user():
    '''问候用户，并且指出名字'''
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("what is your name? ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("we will remember you!" + username + "!")
    else:
        print("Welcome back " + username + "!")

greet_user()
'''
重构-----将用户的信息存储，并判断用户是否已经存储消息
10.4.2
'''
"""
#将上面函数重构
import json

def get_stored_username():
    '''如果用户存储了他，就读取他'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''提示用户输入名字'''
    username = input("What is your name?")
    filename = 'username.json'

    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    '''问候用户，并且指出名字'''
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back," + username + "!")


greet_user()









