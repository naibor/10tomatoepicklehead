<<<<<<< HEAD
from model import edit_comment

edit_comment(0)
=======
from model import User, Comment, Tread
# class User:
#     print('Are you signed up?')
#     signup = input('Select Yes or No:')
#     if signup == No:
#         new_user.signup()
#     else:
#         new_user.login()
    

class comments:
    print('select 1 to post comment')
    print('select 2 to edit comment')
    print('selcet 3 to delete comment')

    user_option = input('enter your option:')

    if user_option == '1':
        new_comment = input("Enter a comment:")
        new_comment = Comment(new_comment)
        new_comment.create_comment()
    elif user_option == '2':
        new_comment.edit_comment()
    elif user_option == '3':
        new_comment.delete_comment()


    
>>>>>>> develop
