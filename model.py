from datetime import datetime

message = 'null'
timestamp = 'null'
ID = 'null'
the_comment = {'message':'hello','timestamp':'now-changethislater','ID':'1'}
the_other_comment = {'message':'helloagain','timestamp':'now-changethislateragain','ID':'2'}

comment_list = [the_comment, the_other_comment]
user_info = []
user_details = {}


def timestamp():
    ourtime = datetime.now()
    return ourtime

def create_id(list):
    id = len(list)+1
    return id

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.timestamp = timestamp()

    
    def signup(self):
        user_details = {"username":self.username, "password": self.password}
        user_info.append(user_details)
        return {"txt": "User Registered"}

    def login(self):
        for every_user in user_info:
            if every_user["username"] == self.username:
                if every_user["password"]== self.password:
                    print("logged in successfully")
                    return True
                else:
                    print("invalid password,consider refactoring")
                    return False
            else:
                print("invalid username,consider signing up")
                return {"txt": "Username does not exist"}
        

class Moderator(User):
    def __init__(self,username,password):
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
                admin = Admin(user.username,user.password)
                return admin


class Comment:
    def __init__(self, message):
        self.message = message
        self.timestamp = timestamp()
        self.ID = len(comment_list) + 1
  
  
    @staticmethod
    def delete_comment(id):
        for comment in comment_list:
            if comment["id"] == id:
                comment_list.remove(comment)
                return "deleted comment"

    def create_comment(self):
        new_comment = {
            "message":self.message,
            "timestamp":self.timestamp,
            "ID":self.ID
        }
        the_comment = new_comment
        comment_list.append(the_comment)
        print (the_comment)

        

class Tread(Comment):

    def __init__(self):
        Comment.__init__(self)
        self.parent_id = self.ID
    def create_thread(self):
        new_thread = {self.parent_id :{
            "message":self.message,
            "timestamp":self.timestamp,
            "ID":self.ID
        }}
        the_comment.append(new_thread)







#Method to edit exisiting comments
def edit_comment(commentID):

    #Letting the user know what is about to be editted
    message_dict = comment_list[commentID]
    print('You are about to edit the post displayed below ')
    print('--------------------------------')
    
    print(message_dict['message'])
    print()
    print()


    #Let the user enter a new message to replace the old one
    newmessage = input('Enter new message: ')
    new_dict = {'message':newmessage,'timestamp':'now-changethislateragain','ID':'2'}
    comment_list[commentID] = new_dict



    #Display the new message to the user
    print('The new edited message reads ')
    print('--------------------------------')
    print()
    print()


    #Confirming the new message is in the list of dicts
    current_message=comment_list[commentID]
    print(current_message['message'])
