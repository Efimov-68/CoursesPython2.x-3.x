import json

'''Форма сбора информации от пользователя'''

def get_stored_user():
    filename = "regform.json"
    try:
        with open(filename, "r") as f_obj:
            regform = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return regform

def get_new_user():
    login = input("Придумайте уникальный логин для вашего профиля: ")
    password = input()
    rep_password = input()
    if rep_password == password:
        print("Пароль совпадает.\n")
        first = input("Введите ваше имя:\n")
        last = input("Введите вашу фамилию:\n")
        email = input("Введите E-mail:\n")
        phone = input("Введите телефон:\n")
        text = input("Ваш комментарий:\n")
    elif rep_password != password:
        print("Пароль не совпадает. Повторите ввод.")
        return rep_password
    regform = {'login': login, 'password': password,\
               'rep_password': rep_password, 'first': first,\
               'last': last, 'email': email, 'phone': phone, 'text': text}
    
    filename = "regform.json"
    with open(filename, "w") as f_obj:
        json.dump(regform, f_obj)
        return regform
    
def greet_user():
    regform = get_stored_user()
    if regform:
        print("Добро пожаловать, " + regform['first'] + "!")
    else:
        regform = get_new_user()
        print("Ваша введеная информация добавлена, приходите к нам еще " \
              + regform['first'] + "!")

greet_user()
