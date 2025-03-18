# ccxt-opensearch
CCXT data storage on Opensearch

## WIP

- Integration with TA-Lib to calculate indicators
- Alerts based on indicators
- Dashboards

## Usage

Simply run this command to run all components in docker-compose.yml file.

```shell
docker compose up -d
```

## Components

To access to the platform use "admin" and its password (docker-compose.yml OPENSEARCH_INITIAL_ADMIN_PASSWORD env var).

- (GUI) OpenSearch Dashboard: http://127.0.0.1:5601 (no certs)
- (API) OpenSearch Index: https://127.0.0.1:9200 (self certs)

## Fetch Data

Install the requirements and execute the script to fetch data and ingest into OpenSearch.

You can run it as a cron task or manually as shown below using the first parameter as the desired symbol. 

Manually (just for testing)

```shell
python3 scripts/fetcher.py SOL/USDT:USDT
python3 scripts/fetcher.py ETH/USDT:USDT
python3 scripts/fetcher.py BTC/USDT:USDT
```

Cron tasks executed each minute

```shell
* * * * * python3 scripts/fetcher.py SOL/USDT:USDT
* * * * * python3 scripts/fetcher.py ETH/USDT:USDT
* * * * * python3 scripts/fetcher.py BTC/USDT:USDT
```

## Data Ingestion

The script writes bulk data in OpenSearch using this index syntax:

```
binance-crypto-btc_usdt_usdt-2025-03-18
binance-crypto-eth_usdt_usdt-2025-03-18
binance-crypto-sol_usdt_usdt-2025-03-18
...
```

This way, you can go Management > Dashboard Management > Index Patterns and then create an index for all assets:

```
binance-crypto-*
```

Or an index for the same asset:

```
binance-crypto-btc-*
```
