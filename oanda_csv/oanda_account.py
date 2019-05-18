import configparser

_CONFIG = configparser.ConfigParser()
_CONFIG.read(r'./config.ini')


def read_oanda_authz():
    return _CONFIG['account']['accountID'], _CONFIG['account']['access_token']


if __name__ == "__main__":
    id, token = read_oanda_authz()
    print("id={}, token={}".format(id, token))
