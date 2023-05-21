import requests, json
from flask import Flask
from datetime import datetime as dtm

app = Flask(__name__)


def get_all_stats():
    url = 'https://api.blockchair.com/bitcoin/stats'
    stats = requests.get(url).json()['data']
    return stats

@app.route("/")
def get_btc_stats():
    stats = get_all_stats()
    price = stats['market_price_usd']
    sfd = int(100E6/price) # #sats for a dollar
    # mtime = '{}:{}'.format(sfd[:-2], sfd[2:]) # moscow time
    blocks, nodes = stats['blocks'], stats['nodes']
    diff = int(stats['difficulty'])
    fee = int(stats['suggested_transaction_fee_per_byte_sat'])
    hrate = int(int(stats['hashrate_24h'])/(10**18)) # exa=10^18
    result = {}
    
    dt = dtm.now().strftime('%a %b %-d')
    ts = dtm.now().strftime('%-I.%M%p')
    result['1'] = f'${price:,}'
    result['2'] = f'#{blocks:,}'
    result['3'] = f'{sfd:,} sats/$'
    result['4'] = f'{fee} sat/vB'
    result['5'] = f'{hrate} EH/s'
    result['6'] = f'{diff:.2E}'
    result['7'] = f'{nodes:,} nodes'
    result['8'] = f'{dt}'
    result['9'] = f'~{ts}'
    
    response = app.response_class(
        response=json.dumps(result),
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=False)