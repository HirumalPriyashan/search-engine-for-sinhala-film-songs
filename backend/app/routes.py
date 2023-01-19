from elasticsearch import helpers
from flask import jsonify, make_response, request
# from pathlib import Path
# import json

from app import app, elastic_client, config, settings, query_builder

client = elastic_client.client
qb = query_builder.QueryBuilder()

@app.route('/search',methods=["POST"])
def search():
    res = []
    if(request.method == "POST"):
        query = request.json.get('query')
        query_body = qb.build_query(query)
        print(query_body)
        res = client.search(index=config.INDEX, query=query_body)
        print("Got %d Hits:" % res['hits']['total']['value'])
        print(res)
        resp = {
            'hits': res['hits']['total']['value'],
            'results': res['hits']['hits']
        }
        return make_response(jsonify(resp), 200)

# folowings are for testing purposes

# @app.route('/health')
# def health():
#     print(client.info())
#     res = client.cluster.health(wait_for_status='yellow', request_timeout=1)
#     return make_response(json.dumps(str(res), indent=2), 200)

# @app.route('/create_index')
# def create_index():
#     res = client.indices.create(config.INDEX, ignore=400, settings=settings.settings)
#     print(res)
#     return make_response('Index created', 200)

# @app.route('/add_data')
# def add_data():
#     path = Path(__file__).parent / ('../elasticsearch/annotated-song-lyrics.json')
#     with open(path, 'r', encoding="utf-8") as file:
#         data = json.load(file)
#     res = helpers.bulk(client, data, index=config.INDEX)
#     return make_response(jsonify(res), 200)

# @app.route('/delete', methods=["DELETE"])
# def delete():
#     res = client.options(ignore_status=[400,404]).indices.delete(index=config.INDEX)
#     print(res)
#     return make_response('Success', 200)
