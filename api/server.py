'''
Resolve an AKA identifier to a location on the web.
'''


import json
from flask import Flask, request, redirect, abort, jsonify
from pathlib import Path
from werkzeug.exceptions import NotAcceptable


app = Flask(__name__)

@app.route('/<identifier>', methods=['GET'])
@app.route('/aka2uri/<identifier>', methods=['GET'])
def resolve(identifier=None):
    '''
    Resolve an AKA identifier.
    '''

    try:
        target = mapping[identifier]
    except KeyError:
        return abort(404)
    
    preferred_content = content_negotiation()
    if preferred_content in ['application/ld+json', 'application/json']:
        linked_art_object = serialise_to_linked_art(identifier, target)
        return jsonify(linked_art_object)
    else:
        return redirect(target, code=302)  


@app.route('/', methods=['POST'])
@app.route('/uri2aka', methods=['POST'])
def resolve_uri():
    try:
        uri = request.json['uri']
        aks_id = mapping[uri]
    except Exception:
        return abort(404)

    preferred_content = content_negotiation()
    if preferred_content == 'application/ld+json':
        # Implementation required?
        pass
    else:
      return aks_id
      
      
def content_negotiation():
    supported_content_types = ['text/html', 'application/ld+json']
    # Select which content type to provide.
    preferred_content = request.accept_mimetypes.best_match(supported_content_types)
    if preferred_content is None:
        # Unacceptable.
        description = '{} Supported entities are: {}'.format(
            NotAcceptable.description, ', '.join(supported_content_types))
        raise NotAcceptable(description)
    return preferred_content


def serialise_to_linked_art(identifier, target):
    linked_art_object = {
        "@context": "https://linked.art/ns/v1/linked-art.json",
        "id": f"https://alsoknownas.glitch.me/{identifier}",
        "type": "Identifier",
        "content": identifier,
        "identifies": [
            {
                "id": target,
                "type": "HumanMadeObject"
            }
        ],
        "classified_as": [
            {
                "id": "http://vocab.getty.edu/aat/300435704",
                "type": "Type",
                "_label": "record identifiers"
            }
        ]
    }
    return linked_art_object
  

if __name__ == '__main__':
    mapping = {}
    for mapping_file in Path('.').glob('mapping*.json'):
        with open(str(mapping_file)) as data:
            local_mapping = json.load(data)
            for key in local_mapping:
                value = local_mapping[key]
                mapping[key] = value
                mapping[value] = key
    app.run()
