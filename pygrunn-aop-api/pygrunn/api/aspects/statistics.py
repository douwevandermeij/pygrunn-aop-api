
def statistics(function):
    def advice(*args, **kwargs):
        """
        Increase the usage count of the API for the user logged in
        """
        # TODO: make implementation as stated above
        return function(*args, **kwargs)
    return advice
