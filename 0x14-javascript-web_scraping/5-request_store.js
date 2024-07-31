#!/usr/bin/node

// Import required modules
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the provided URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  // Write the response body to the specified file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf8', err => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    console.log(`${filePath}`);
  });
});
