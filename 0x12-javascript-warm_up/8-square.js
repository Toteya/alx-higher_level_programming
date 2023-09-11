#!/usr/bin/node

const process = require('process');

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < process.argv[2]; i++) {
    line += 'x';
  }
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(line);
  }
}
