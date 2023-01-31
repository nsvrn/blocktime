# from fetch_data import helper as hp
#
# def get_price():
#     price = hp.get_value('btc_price.json', dtype='int')
#     return price

import requests


def get_all_stats():
    url = 'https://api.blockchair.com/bitcoin/stats'
    stats = requests.get(url).json()['data']
    return stats


def get_btc_stats():
    stats = get_all_stats()
    price = stats['market_price_usd']
    sfd = str(int(100E6/price)) # #sats for a dollar
    mtime = '{}:{}'.format(sfd[:-2], sfd[2:]) # moscow time
    blocks, nodes = stats['blocks'], stats['nodes']
    diff = int(stats['difficulty'])
    fee = int(stats['suggested_transaction_fee_per_byte_sat'])
    hrate = int(int(stats['hashrate_24h'])/(10**18)) # exa=10^18
    result = {}
    result['height'] = f'#{blocks:,}'
    result['price'] = f'${price:,}'
    result['mtime'] = mtime
    result['fee'] = f'{fee} sat/vB'
    result['hrate'] = f'{hrate} EH/s'
    result['diff'] = f'{diff:.2E}'
    result['nodes'] = f'{nodes:,} nodes'
    return result
    
