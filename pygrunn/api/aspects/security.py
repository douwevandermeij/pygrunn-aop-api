
def security(function):
    def advicee(*args, **kwargs):
        """
        Check if the token is (still) valid
        Check if the number of API calls has not exceeded the maximum
        """
        # TODO: make checks as stated above
        from flask import request
        if 'token' in request.args and request.args['token'] == 'abc':
            return function(*args, **kwargs)
        raise Exception('No valid token provided')
    return advicee
