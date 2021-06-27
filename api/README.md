# Glitch Application

Resolve an Also Known As identifier:

```bash
curl -L https://alsoknownas.glitch.me/beleefd-lauw-tekening-ding
```

Resolve a URI to Also Known As identifier:

```
curl -X POST https://alsoknownas.glitch.me/ \
    --header "Content-Type: application/json" \
    --data '{"uri": "https://pid.uba.uva.nl/ark:/88238/b1990032751780205131"}'
```
