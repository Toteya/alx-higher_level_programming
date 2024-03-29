#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];
const characterId = '18';

request(url, (error, response, body) => {
  if (error) console.error(error);
  const details = JSON.parse(body);
  const films = details.results;
  let numOfAppearances = 0;
  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      const arr = character.split('/');
      if (arr.includes(characterId)) {
        numOfAppearances++;
      }
    }
  }
  console.log(numOfAppearances);
});
