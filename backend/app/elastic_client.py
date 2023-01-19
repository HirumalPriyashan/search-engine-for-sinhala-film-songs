from elasticsearch import Elasticsearch
from app import config

client = Elasticsearch(
    config.ELASTIC_URL
    # ca_certs=config.CERT_PATH,
    # basic_auth=(config.ELASTIC_USERNAME, config.ELASTIC_PASSWORD)
)

if __name__ == "__main__":
    print(client.info())
