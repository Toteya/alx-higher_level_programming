#!/usr/bin/node

function factorial (num) {
  if (num > 1) {
    return num * factorial(num - 1);
  } else {
    return 1;
  }
}

const process = require('process');
const myNum = Number(process.argv[2]);
console.log(factorial(myNum));
