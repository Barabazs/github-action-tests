from utils import config


def hello():
    return "GM World!"


def use_config():
    print(config.ENDPOINT)
    print("GM world")
    return config.ENDPOINT


def return_all_keys():
    keys = {
        "ENDPOINT": config.ENDPOINT,
        "ARBITRUM_ENDPOINT": config.ARBITRUM_ENDPOINT,
        "AVALANCHE_ENDPOINT": config.AVALANCHE_ENDPOINT,
        "BINANCE_ENDPOINT": config.BINANCE_ENDPOINT,
        "FANTOM_ENDPOINT": config.FANTOM_ENDPOINT,
        "OPTIMISM_ENDPOINT": config.OPTIMISM_ENDPOINT,
        "POLYGON_ENDPOINT": config.POLYGON_ENDPOINT,
    }
    return keys
