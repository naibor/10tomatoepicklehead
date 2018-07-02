from datetime import datetime

comment_list = []
the_comment = {}
user_info = []
user_details = {}


def timestamp():
    ourtime = str(datetime.now())
    # ourtime = datetime.strptime(ourtime, '%d%b%Y')
    return ourtime


class User:
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    #     self.timestamp = timestamp()

    @staticmethod
    def signup(username, password, moderator=False, admin=False):
        user_details[username] = {"password": password, "moderator": moderator, "admin": admin}
        user_info.append(user_details)
        return {"txt": "User Registered"}

    @staticmethod
    def login(username, password):
        if username in user_details:
            if user_details[username]["password"] == password:
                return {"txt": "Logged In"}
            else:
                return {"txt": "Invalid Password"}
        else:
            return {"txt": "Invalid Username"}


class Moderator(User):
    def __init__(self, username, password):
        User.__init__(self)
        self.is_moderator = True


class Admin(Moderator):
    def __init__(self, username, password):
        Moderator.__init__(self, username, password)
        self.is_admin = True


class Comment:
    def __init__(self, message):
        self.message = message
        self.timestamp = timestamp()
        self.ID = len(comment_list) + 1


class Tread(Comment):
    def __init__(self, message):
        Comment.__init__(self, message)
        self.parent_id = self.ID


user = User()
user.signup("Antony Kavoo", "123", True, False)
user.signup("Phillip", "456")
print(user_details)
print(user.login("Antony Kavoo", "123"))
print(user_info)

