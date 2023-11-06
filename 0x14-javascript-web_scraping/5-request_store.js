#!/usr/bin/node
// requests the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];
let data;

request(url, (error, respone, body) => {
  if (error) console.error(error);
  data = body;

  fs.writeFile(filepath, data,
    {
      encoding: 'utf8'
    },
    (err) => {
      if (err) {
        console.error(err);
      }
    });
});

/*
fs.writeFile(filepath, data, err => {
  if (err) {
    console.error(err);
  }
});
*/
