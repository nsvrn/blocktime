import requests, json
from pathlib import Path
from bs4 import BeautifulSoup
from loguru import logger


def get_soup(url):
    soup = None
    try:
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    except Exception as e:
        logger.exception(str(e))
    return soup


def _get_value_by_attr(url, name, attr, key):
    value = None
    try:
        value = get_soup(url).find(name, {attr:key}).contents[0]
    except Exception as e:
        logger.exception(str(e))
    return value


def get_value(filename, dtype='str'):
    data = None
    fpath = Path(__file__).parents[0].joinpath(filename)
    with open(fpath) as file:
        data = json.load(file)
    for r in data:
        value = _get_value_by_attr(r['url'], r['name'], r['attr'], r['key'])
        if value:
            value = value.strip()
            logger.info(f"url used: {r['url']}")
            break
    if value and dtype in ['float', 'int']:
        rchars = ['$', ',']
        for r in rchars: value = value.replace(r, '')
        value = float(value.strip())
    if dtype == 'int': value = int(value)
    return value

