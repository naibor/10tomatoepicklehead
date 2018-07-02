from datetime import datetime

message = 'null'
timestamp = 'null'
ID = 'null'


#comment_list = [{message:'hello',timestamp:'now-changethislater',ID:1},{message:'hello',timestamp:'now-changethislater',ID:2}]

the_comment = {'message':'hello','timestamp':'now-changethislater','ID':'1'}
the_other_comment = {'message':'helloagain','timestamp':'now-changethislateragain','ID':'2'}


comment_list = [the_comment, the_other_comment]
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

class Thread(Comment):
    def __init__(self):
        Comment.__init__(self)
        self.parent_id = self.ID




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


