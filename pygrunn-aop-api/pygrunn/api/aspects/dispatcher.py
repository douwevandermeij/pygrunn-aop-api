from pygrunn.api.lib import extract
from pygrunn.core.login import create_token
from pygrunn.core.logic.calculations import add, sub, mult, div, something_cool


MAPPING = {
    'add': (add, ['lhs', 'rhs']),
    'sub': (sub, ['lhs', 'rhs']),
    'mult': (mult, ['lhs', 'rhs']),
    'div': (div, ['lhs', 'rhs']),
    'something_cool': (something_cool, ['function', 'token']),
    'create_token': (create_token, ['username', 'password']),
}


def specific_dispatch(specific_function_name):
    def inner(function):
        def decorator(*args, **kwargs):
            kwargs['function'] = specific_function_name
            return function(*args, **kwargs)
        return decorator
    return inner


def dispatcher(function):
    def advice(request, *args, **kwargs):
        if 'function' in kwargs:
            if kwargs['function'] in MAPPING:
                core_function, params = MAPPING[kwargs['function']]
                kwargs.update(extract(params, request.GET))
                return function(proxy=core_function, params=params, *args, **kwargs)
            raise Exception('Function "{0}" is not an API function'.format(kwargs['function']))
        raise Exception('Parameter "function" not provided')
    return advice
