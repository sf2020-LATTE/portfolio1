# settings/production.py

from .base import *

#デプロイ用設定
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'jw-1j!-!_g7v1ufh+g+umj55bmgh*6$@e8^+be#f!%h=limfr_'
SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []