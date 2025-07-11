import os

def get_env():
    return os.getenv("APP_ENV", "undefined")