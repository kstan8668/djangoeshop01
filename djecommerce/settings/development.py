from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'djangoeshop01.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STRIPE_PUBLIC_KEY = 'pk_test_frtoSCH35rMpvM02Emzlzrg3005iBwDOog'
STRIPE_SECRET_KEY = 'sk_test_BNjMItExNeEoEWU97Fl4CXYH00rQvQ1HuH'
