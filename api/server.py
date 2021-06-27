'''
Resolve an AKA identifier to a location on the web.
'''


import json
from flask import Flask, request, redirect, abort
from pathlib import Path


app = Flask(__name__)

@app.route('/<identifier>', methods=['GET'])
@app.route('/aka2uri/<identifier>', methods=['GET'])
def resolve(identifier=None):
    '''
    Resolve an AKA identifier.
    '''
    try:
        target = mapping[identifier]
        return redirect(target, code=302)    
    except KeyError:
        return abort(404)


@app.route('/', methods=['POST'])
@app.route('/uri2aka', methods=['POST'])
def resolve_uri():
    try:
        uri = request.json['uri']
        aks_id = mapping[uri]
        return aks_id
    except Exception:
        return abort(404)


if __name__ == '__main__':
    mapping = {}
    for mapping_file in Path('.').glob('mapping*.json'):
        print(mapping_file)
        with open(str(mapping_file)) as data:
            local_mapping = json.load(data)
            for key in local_mapping:
                value = local_mapping[key]
                mapping[key] = value
                mapping[value] = key
    app.run()
