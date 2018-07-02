from datetime import datetime

comment_list = []
the_comment = {}
user_info = []
user_details = {}

def timestamp():
    ourtime = datetime.now()
    ourtime=datetime.strptime(ourtime, '%d%b%Y')
    return ourtime

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.timestamp = timestamp()

class Moderator(User):
    def __init__(self):
        User.__init__(self,username,password)
        self.is_moderator = True

class Admin(Moderator):
    def __init__(self):
        Moderator.__init__(self)
        self.is_admin = True


class Comment:
    def __init__(self,message):
        self.message = message
        self.timestamp = timestamp()
        self.ID = len(comment_list) + 1

class Tread(Comment):
    def __init__(self):
        Comment.__init__(self)
        self.parent_id = self.ID


