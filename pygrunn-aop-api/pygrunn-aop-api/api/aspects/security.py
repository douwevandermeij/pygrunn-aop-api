
def security(function):
    def advice(request, *args, **kwargs):
        """
        Check if the token is (still) valid
        Check if the number of API calls has not exceeded the maximum
        """
        # TODO: make checks as stated above
        if 'token' in request.GET and request.GET['token'] == 'abc':
            return function(request, *args, **kwargs)
        raise Exception('No valid token provided')
    return advice
