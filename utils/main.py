from utils import config


def hello():
    return "GM World!"


def use_config():
    print(config.ENDPOINT)
    return config.ENDPOINT
