const MAPPING_BLM_URI2AKA = {
    "https://katalog.landesmuseum.de/object/OTQvNzEy": "nettes-rundes-silber-ding",
    "https://katalog.landesmuseum.de/object/QyAxMTAwNCBj": "amüsantes-vollkommenes-keramik-ding",
    "https://katalog.landesmuseum.de/object/NjgvMTE3IGE=": "schmales-unfreundliches-bronze-ding",
    "https://katalog.landesmuseum.de/object/QyA2MDU4": "billiges-herrliches-sandstein-ding",
    "https://katalog.landesmuseum.de/object/QiAx": "dankbares-umweltfeindliches-keramik-ding",
    "https://katalog.landesmuseum.de/object/QyAxMTE4MiBh": "riesiges-lautloses-glas-ding",
    "https://katalog.landesmuseum.de/object/MjAwOC82MzY=": "lustiges-grobes-keramik-ding",
    "https://katalog.landesmuseum.de/object/QyAzNDU0": "cooles-hartes-bronze-ding",
    "https://katalog.landesmuseum.de/object/NzMvMTcxIGI=": "intelligentes-hartnäckiges-silber-ding",
    "https://katalog.landesmuseum.de/object/S2xlIDcvMzY=": "aufgeregtes-rücksichtsvolles-bein-ding"
}

const MAPPING_AP_URI2AKA = {
    "https://katalog.landesmuseum.de/object/OTQvNzEy": "nettes-rundes-silber-ding",
    "https://katalog.landesmuseum.de/object/QyAxMTAwNCBj": "amüsantes-vollkommenes-keramik-ding",
    "https://katalog.landesmuseum.de/object/NjgvMTE3IGE=": "schmales-unfreundliches-bronze-ding",
    "https://katalog.landesmuseum.de/object/QyA2MDU4": "billiges-herrliches-sandstein-ding",
    "https://katalog.landesmuseum.de/object/QiAx": "dankbares-umweltfeindliches-keramik-ding",
    "https://katalog.landesmuseum.de/object/QyAxMTE4MiBh": "riesiges-lautloses-glas-ding",
    "https://katalog.landesmuseum.de/object/MjAwOC82MzY=": "lustiges-grobes-keramik-ding",
    "https://katalog.landesmuseum.de/object/QyAzNDU0": "cooles-hartes-bronze-ding",
    "https://katalog.landesmuseum.de/object/NzMvMTcxIGI=": "intelligentes-hartnäckiges-silber-ding",
    "https://katalog.landesmuseum.de/object/S2xlIDcvMzY=": "aufgeregtes-rücksichtsvolles-bein-ding"
}

const fetchAKA = async () => {
    console.log("fetchAKA")

    // this next line currently gives an error:
    // Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://alsoknownas.glitch.me/. (Reason: CORS header ‘Origin’ cannot be added).
    const response = await fetch('https://alsoknownas.glitch.me/', {
      method: 'POST',
      body: {
          'uri': document.location.href
      }, // string or object
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/ld+json'
      }
    });
    const myJson = await response.json(); //extract JSON from the http response

    console.log("awaiting...");
    // do something with myJson
    console.log(myJson)
    // const identifier = myJson['identifies'][0]['id'];


  }

console.log("hello!!!");
fetchAKA();

var container = document.createElement('div');
container.style.position = 'absolute';
container.style.bottom = '50px';
container.style.right = '50px';
container.style.backgroundColor = '#fff';
container.style.borderRadius = '10px';
container.style.padding = '20px';
container.style.boxShadow = '0px 0px 20px rgba(0,0,0,0.3)';
container.style.textAlign = 'center';

var hello = document.createElement('div');
hello.textContent = `👋`;
hello.style.fontWeight = '900';
hello.style.fontSize = '4rem';

var header = document.createElement('h2');
header.textContent = `This object is ✨Also Known As✨`;
header.style.fontSize = '2rem';

var aka = document.createElement('h2');
aka.textContent = `${MAPPING_BLM_URI2AKA[document.location.href]}`;

var infoLink = document.createElement('a');
infoLink.textContent = `ℹ️ more info`;
infoLink.href = `https://github.com/edwardanderson/also-known-as`;
infoLink.target = `_blank`;

container.appendChild(hello)
container.appendChild(header)
container.appendChild(aka)
container.appendChild(infoLink)
document.body.appendChild(container);
