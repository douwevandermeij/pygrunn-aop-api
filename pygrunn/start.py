from flask import Flask
app = Flask(__name__)

import sys
sys.path.append('/pygrunn')

from api.aspects.dispatcher import dispatcher, specific_dispatch
from api.aspects.response import response
from api.aspects.security import security
from api.aspects.statistics import statistics
from api.lib import extract


def _proxy(*args, **kwargs):
    proxy = kwargs['proxy']
    params = kwargs['params']
    return str(proxy(**extract(params, kwargs)))


@response
@specific_dispatch('create_token')
@dispatcher
def create_token(*args, **kwargs):
    return _proxy(*args, **kwargs)


@security
@response
@statistics
@dispatcher
def api_call(*args, **kwargs):
    return _proxy(*args, **kwargs)


app.add_url_rule('/api/<format>/create_token/', view_func=create_token)
app.add_url_rule('/api/<format>/<function>/', view_func=api_call)


if __name__ == '__main__':
    app.run()