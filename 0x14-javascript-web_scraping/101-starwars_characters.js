#!/usr/bin/node
const request = require('request');
const process = require('process');
const movieId = process.argv[2];
const requestURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(requestURL, (error, response) => {
  if (error) return console.log(error);
  const results = JSON.parse(response.body);
  const movieCharacters = results.characters;
  printCharacters(movieCharacters, 0);
});

const printCharacters = (characters, index) => {
  characters.forEach((character) => {
    request.get(character, (error, response) => {
      if (error) return console.log(error);
      const character = JSON.parse(response.body);
      console.log(character.name);
      if (index + 1 < characters.length) {
        printCharacters(characters, (index += 1));
      }
    });
  });
};
