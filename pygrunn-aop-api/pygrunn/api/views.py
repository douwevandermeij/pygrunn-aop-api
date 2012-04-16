"""
Module that provides API functionality
"""
from pygrunn.api.aspects.dispatcher import dispatcher, specific_dispatch
from pygrunn.api.aspects.response import response
from pygrunn.api.aspects.security import security
from pygrunn.api.aspects.statistics import statistics
from pygrunn.api.lib import extract


def _proxy(*args, **kwargs):
    proxy = kwargs['proxy']
    params = kwargs['params']
    return proxy(**extract(params, kwargs))


@security
@response
@statistics
@dispatcher
def api_call(*args, **kwargs):
    return _proxy(*args, **kwargs)


@response
@specific_dispatch('create_token')
@dispatcher
def create_token(*args, **kwargs):
    return _proxy(*args, **kwargs)
