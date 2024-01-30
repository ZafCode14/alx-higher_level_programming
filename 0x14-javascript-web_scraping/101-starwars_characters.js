#!/usr/bin/node
const request = require('request');

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve({ response, body });
      }
    });
  });
}

async function fetchAndPrintNames (urlFilm) {
  try {
    const filmResponse = await getRequest(urlFilm);
    const filmData = JSON.parse(filmResponse.body);

    for (const characterUrl of filmData.characters) {
      const characterResponse = await getRequest(characterUrl);
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const urlFilm = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
fetchAndPrintNames(urlFilm);
