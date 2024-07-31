#!/usr/bin/node

// Import the request module
const request = require('request');

const url = process.argv[2];
const wedgeAntillesId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(film => {
      if (film.characters && film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    console.log(`${count}`);
  }
});
