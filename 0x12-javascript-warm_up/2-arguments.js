#!/usr/bin/node
const process = require('process');
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  sonsole.log('Argument found');
} else {
  console.log('Arguments found');
}
