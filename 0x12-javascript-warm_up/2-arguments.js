#!/usr/bin/node
// import { argv } from 'node:process';
const process = require('process');

if (process.argv.length < 3) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
