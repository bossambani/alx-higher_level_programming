#!/usr/bin/node

// import the module
const fs = require('fs');

// assigns the file path to the variable
const file = process.argv[2];

// read the file

try {
  const data = fs.readFileSync(file, 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
