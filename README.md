# ccxt-opensearch
CCXT data storage on Opensearch

## Usage

Simply run this command to run all components in docker-compose.yml file.

```shell
docker compose up -d
```

## Components

To access to the platform use "admin" and its password (docker-compose.yml OPENSEARCH_INITIAL_ADMIN_PASSWORD env var).

- (GUI) Opensearch Dashboard: http://127.0.0.1:5601 (no certs)
- (API) Opensearch Index: https://127.0.0.1:9200 (self certs)
