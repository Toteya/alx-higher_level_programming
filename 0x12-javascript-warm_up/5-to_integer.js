#!/usr/bin/node

const process = require('process');
const myInt = Number(process.argv[2]);
if (isNaN(myInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myInt));
}
