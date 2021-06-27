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

var header = document.createElement('p');
header.textContent = 'this is where the identifier should go';
document.body.appendChild(header);
header.style.position = 'absolute';
header.style.bottom = '50px';
header.style.right = '50px';
