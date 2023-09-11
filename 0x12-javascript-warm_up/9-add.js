#!/usr/bin/node

function add (x, y) {
  return x + y;
}

const process = require('process');
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
console.log(add(num1, num2));
