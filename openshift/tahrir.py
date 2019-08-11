import sys
sys.stdout = sys.stderr

import __main__
__main__.__requires__ = __requires__ = ['tahrir', 'sqlalchemy>=0.8']
import pkg_resources
pkg_resources.require(__requires__)

import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/.python-eggs'
os.environ['SQLALCHEMY_URL'] = '%s://%s:%s@%s/%s' % \
    (os.getenv('DATABASE_ENGINE'), \
    os.getenv('DATABASE_USER'), \
    os.getenv('DATABASE_PASSWORD'), \
    os.getenv('DATABASE_SERVICE_NAME'), \
    os.getenv('DATABASE_NAME'))

from pyramid.paster import get_app, setup_logging
d = os.path.dirname(os.path.realpath(__file__))
ini_path = d + '/default.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
