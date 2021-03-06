# Author Tsuneda Toi - refresh_token
# Author Nagai Ryusei - all except Tsuneda's part
from . import auth

def signup(email, password):
    """
    Parameters:
        email
        password
    Returns:
        access_token
        user_id
    """
    user = auth.create_user_with_email_and_password(email, password)
    access_token = user['idToken']
    user_id = user['localId']
    print(user)
    return access_token, user_id

def signin(email, password):
    """
    Parameters:
        email
        password
    Returns:
        access_token
    """
    user = auth.sign_in_with_email_and_password(email, password)
    print(user)
    access_token = user['idToken']
    print(user)
    user_id = user['localId']
    return user_id #access_token

def verify(access_token):
    """
    Parameters:
        access_token
    Returns:
        user_id
    """
    user = auth.get_account_info(access_token)
    print(user)
    try:
        user = auth.get_account_info(access_token)
        print(user)
        user_id = user['users'][0]['localId']
        return user_id
    except:
        return ""

def refresh_token(access_token):
    """
    Parameters:
        access_token
    Returns:
        user_id
    """
    try:
        user = auth.refresh(access_token)
        new_token = user['users'][0]["refresh_token"]
        return new_token
    except:
        return ""

