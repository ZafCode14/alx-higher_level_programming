#!/usr/bin/node
const request = require('request');
const urlFilm = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(urlFilm, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const data = JSON.parse(body);
    data.characters.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response) {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});
