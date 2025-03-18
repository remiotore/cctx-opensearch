# pip install ccxt opensearch-py

import ccxt
import warnings
import argparse
from datetime import datetime, timedelta
from opensearchpy import OpenSearch, helpers


warnings.simplefilter("ignore")


parser = argparse.ArgumentParser(description="Fetch previous minute OHLCV data for a symbol from Binance.")
parser.add_argument('symbol', type=str, help='The trading pair symbol (e.g., BTC/USDT)')
args = parser.parse_args()




timeframe = '1m'

previous_minute = datetime.utcnow() - timedelta(minutes=1)
since = int(previous_minute.timestamp() * 1000)

symbol = args.symbol
index = symbol.replace('/', '_').replace(':', '_').lower()
today = previous_minute.strftime("%Y-%m-%d")
name  = f"{index}-{today}"

binance = ccxt.binance()
ohlcv = binance.fetch_ohlcv(symbol, timeframe, since=since)

documents = []

for record in ohlcv:
    document = {
        "_index"     : f"binance-crypto-{name}",
        "@timestamp" : datetime.utcfromtimestamp(record[0] / 1000).isoformat(), 
        'open'       : record[1],
        'high'       : record[2],
        'low'        : record[3],
        'close'      : record[4],
        'volume'     : record[5],
        'symbol'     : symbol
    }
    documents.append(document)
    
opensearch_client = OpenSearch(
    hosts = [{'host': '127.0.0.1', 'port': 9200}],
    http_auth=('admin', '!SuperS3cr3tPassword!'), 
    verify_certs=False,
    use_ssl=True,
)
success, failed = helpers.bulk(opensearch_client, documents, max_retries=3)

print(success)
print(failed)