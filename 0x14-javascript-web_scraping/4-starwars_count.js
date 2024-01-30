#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(18)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
