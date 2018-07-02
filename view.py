from model import User, Admin, Moderator, Comment, Tread, user_info




def comments():
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

class User:
    print('New user?')
    signup = input('Select Yes or No:')
    if signup == 'No':
        username = input('enter username:')
        password = input('enter password:')
        new_user = User(username,password)
        is_sign_up = new_user.signup()
        print('You have signed up')
        username = input('enter username:')
        password = input('enter password:')

        logged_in = new_user.login()
        if logged_in:
                comments()
    else:
        """user login"""
        username = input('enter username:')
        password = input('enter password:')
        login = new_user.login()
        if login:
            comments()
    