import configparser
from pathlib import Path


def _get_conf(filename):
    config = configparser.ConfigParser()
    fpath = Path(__file__).parents[0].joinpath(filename)
    config.read(fpath)
    return config._sections


def get_settings(section=None):
    filename = 'settings.conf'
    settings = _get_conf(filename)
    if section: settings = settings[section]
    return settings