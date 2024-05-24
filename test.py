class User:

    def __init__(self, u, r):
        self.user = u
        self.role = r

class Access:

    __access_list = ['admin', 'developer']

    @staticmethod
    def __check_access(rol):
        return rol in Access.__access_list
        
    @staticmethod
    def get_access(ob):
        if isinstance(ob, User):
            if Access.__check_access(ob.role):
                print(f'User {ob.user}: success')
            else:
                print('AccessDenied')
        else:
            print('AccessTypeError')
            


user1 = User('batya99', 'admin')
Access.get_access(user1) # печатает "User batya99: success"

zaya = User('milaya_zaya999', 'user')
Access.get_access(zaya) # печатает AccessDenied

Access.get_access(5) # печатает AccessTypeError