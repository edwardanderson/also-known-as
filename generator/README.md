# Generate mappings from adjectives and URIs

First, we generate permutations of adjectives:

```sh
python make-permutations.py adjectives-dutch.txt permutations-dutch.txt
```

use --german flag to add -es suffix to German adjectives

```sh
python make-permutations.py adjectives-german.txt permutations-german.txt --german
```

With the permutations generated, we can now generate mappings:

```sh
python mint-aka-ids.py ./uris-types-allard-pierson.csv ./permutations-dutch.txt mapping-ap-uri2aka.json mapping-ap-aka2uri.json
```

```sh
python mint-aka-ids.py ./uris-types-blm.csv ./permutations-german.txt mapping-blm-uri2aka.json mapping-blm-aka2uri.json
```