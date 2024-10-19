#!/usr/bin/node

// Import the module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

const dictionary = {};

// Make an HTTP GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  try {
    const data = JSON.parse(body);

    if (!Array.isArray(data)) {
      throw new Error('Expected an array of results');
    }

    data.forEach(result => {
      if (result.completed === true) {
        const userId = result.userId;
        if (!(userId in dictionary)) {
          dictionary[userId] = 0;
        }
        dictionary[userId] += 1;
      }
    });

    console.log(dictionary);
  } catch (parseError) {
    console.error('parseError');
    process.exit(1);
  }
});
