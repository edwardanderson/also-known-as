const userAction = async () => {
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
    // do something with myJson
    console.log("test!!!")
    console.log(myJson)
    const identifier = myJson['identifies'][0]['id'];

  }
  

var header = document.createElement('p');
header.textContent = 'this is where the identifier should go';
document.body.appendChild(header);
header.style.position = 'absolute';
header.style.bottom = '50px';
header.style.right = '50px';
