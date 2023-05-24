import requests, json
from flask import Flask
from datetime import datetime as dtm
import pytz

app = Flask(__name__)


def get_all_stats():
    url = 'https://api.blockchair.com/bitcoin/stats'
    stats = requests.get(url).json()['data']
    return stats

def get_btc_stats(shorten=False, skip_keys=[]):
    stats = get_all_stats()
    price = stats['market_price_usd']
    sfd = int(100E6/price) # #sats for a dollar
    # mtime = '{}:{}'.format(sfd[:-2], sfd[2:]) # moscow time
    blocks, nodes = stats['blocks'], stats['nodes']
    diff = int(stats['difficulty'])
    fee = int(stats['suggested_transaction_fee_per_byte_sat'])
    hrate = int(int(stats['hashrate_24h'])/(10**18)) # exa=10^18
    result = {}
    
    tz = pytz.timezone('US/Eastern')
    dt = dtm.now(tz).strftime('%a %b %-d')
    ts = dtm.now(tz).strftime('%-I.%M%p')
    
    result['height'] = f'#{blocks:,}'
    result['price'] = f'${price:,}'
    result['sats_per_dollar'] = f'{sfd:,} s/$'
    result['fee'] = f'{fee} s/vB'
    result['hrate'] = f'{hrate} EH/s'
    result['diff'] = f'{diff:.2E}'
    result['nodes'] = f'{nodes:,} nodes'
    result['dt'] = f'{dt}'
    result['ts'] = f'~{ts}'

    if shorten: result['dt'] = dtm.now(tz).strftime('%a %m/%-d')
    for k in skip_keys: del result[k]

    return result
    

@app.route("/t5s")
def t5s():
    '''
        for lilygo t5s 2.7 inch eink display
    '''
    result = get_btc_stats()
    response = app.response_class(
        response=json.dumps(result),
        mimetype='application/json'
    )
    return response


@app.route("/t5")
def t5():
    '''
        For lilygo t5 2.13 inch eink display
    '''
    sk = ['diff', 'nodes'] # skip keys
    result = get_btc_stats(shorten=True, skip_keys=sk)
    
    response = app.response_class(
        response=json.dumps(result),
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=False)