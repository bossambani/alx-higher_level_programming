#!/usr/bin/node

// import the module
const request = require('request');

// The first argument is the movie ID
const url = process.argv[2];

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // check for errors during the request
  if (error) {
    console.error(error);
  } else {
    const content = JSON.parse(body).results;
    const moviesWithWedge = content.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // if found
        : count; // if not found
    }, 0);
    console.log(moviesWithWedge);
  }
});
