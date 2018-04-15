import os
import configparser

config = configparser.ConfigParser()
WORK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if os.environ.get("TWITTUS_CONFIG"):
    config.read(os.environ["TWITTUS_CONFIG"])
else:
    config.read(os.path.join(WORK_DIR, 'twittus.conf'))

CONSUMER_KEY = config.get('twitter', 'consumer_key')
CONSUMER_SECRET = config.get('twitter', 'consumer_secret')
ACCESS_TOKEN = config.get('twitter', 'access_token')
ACCESS_TOKEN_SECRET = config.get('twitter', 'access_token_secret')
