# Glitch Application

Dereference an Also Known As identifier:

```bash
curl -L https://alsoknownas.glitch.me/beleefd-lauw-tekening-ding
```

Resolve an Also Known As identifier to Linked Art JSON-LD:

```bash
curl https://alsoknownas.glitch.me/beleefd-lauw-tekening-ding \
    -H "Accept: application/ld+json"
```

Resolve a URI to Also Known As identifier:

```
curl -X POST https://alsoknownas.glitch.me/ \
    --header "Content-Type: application/json" \
    --data '{"uri": "https://pid.uba.uva.nl/ark:/88238/b1990032751780205131"}'
```
