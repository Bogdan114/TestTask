class login_password:
    def __init__(self):
        self.login = ''
        self.password = ''

    def set(self, name, pas):
        self.login = name
        self.password = pas
        if len(self.login) != 0 and len(self.password) != 0:
            return True
        else:
            return False

    def ret_login(self):
        return self.login

    def ret_pass(self):
        return self.password
