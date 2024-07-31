#!/usr/bin/node

// import the module
const request = require('request');
const fs = require('fs');

// The first argument is the URL to request (GET)
const url = process.argv[2];

// The file path
const file = process.argv[3];

// Make an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  // check for errors during the request
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf-8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
