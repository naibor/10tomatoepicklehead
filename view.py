from model import User, Admin, Moderator, Comment, Tread

admin = Admin()
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
    print('Are you signed up?')
    signup = input('Select Yes or No:')
    if signup == No:
        username = input('enter username:')
        password = input('enter password:')
        new_user = User(username,password)
        is_sign_up = new_user.signup()
        
    else:
        username = input('enter username:')
        password = input('enter password:')
        new_user.login(username,password)
        if is_login["txt"] == "Logged In":
            comments()
    

    


    
