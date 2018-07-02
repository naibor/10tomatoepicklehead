from datetime import datetime

comment_list = []
the_comment = {}
user_info = []

def timestamp():
    ourtime = datetime.now()
    #ourtime=datetime.strptime(ourtime, '%d%b%Y')
    return ourtime

def create_id(list):
    id = len(list)+1
    return id


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.timestamp = timestamp()

class Moderator(User):
    def __init__(self, username, password):
        User.__init__(self,username,password)
        self.is_moderator = True

class Admin(Moderator):
    def __init__(self, username, password):
        Moderator.__init__(self, username, password)
        self.is_admin = True

    @staticmethod
    def assign_moderator(username):
         for user in user_info:
            if user["name"] == username:
                moderator = Moderator(user.username,user.password)
                return moderator

    @staticmethod
    def assign_admin(username):
        for user in user_info:
            if user["name"] == username:
                admin = Moderator(user.username,user.password)
                return admin


class Comment:
    def __init__(self,message):
        self.message = message
        self.timestamp = timestamp()
        self.ID = len(comment_list) + 1

    @staticmethod
    def delete_comment(id):
        for comment in comment_list:
            if comment["id"] == id:
                comment_list.remove(comment)
                return "deleted comment"
        

class Tread(Comment):
    def __init__(self):
        Comment.__init__(self)
        self.parent_id = self.ID





