

from user import User

def create_user(first_name, last_name, username, password):
    newuser = User(first_name, last_name, username, password)
    return newuser
def save_user(user):
    user.save.user()
