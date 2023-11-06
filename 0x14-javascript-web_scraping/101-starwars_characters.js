#!/usr/bin/node
// Computes the number of tasks completed bu user id

const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) console.error(error);
  const details = JSON.parse(body);
  const characters = details.characters;
  for (const characterURL of characters) {
    printCharacterName(characterURL);
  }
});

function printCharacterName (charURL) {
  request(charURL, (error, response, body) => {
    if (error) console.error(error);
    const person = JSON.parse(body);
    console.log(person.name);
  });
}
