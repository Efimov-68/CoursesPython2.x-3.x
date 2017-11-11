from reg_function import greet_user

class RegistrationSingIn():
    '''Вход в профиль'''
    def __init__(self, login, password, email, phone, date, first, last, middle = ""):
        self.login = login
        self.password = password
        self.first = first
        self.last = last
        self.maiddle = middle
        self.email = email
        self.phone = phone
        self.date = date
        
    def singIn_user(self):
        filename = "regform.json"
        with open(filename, "r") as f_obj:
            print("\n" + f_obj + "\n")
