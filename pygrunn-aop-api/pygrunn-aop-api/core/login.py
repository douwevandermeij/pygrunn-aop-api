
def create_token(username, password):
    if username and password:
        return '1234567890'
    raise Exception('No username and/or password provided')
