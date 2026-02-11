import configparser

config = configparser.ConfigParser()
config.read("config/defaults.conf")

def get_default(key):
    return config["DEFAULT"].get(key)