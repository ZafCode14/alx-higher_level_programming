#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const data = JSON.parse(body);
    const dict = {};
    data.forEach((user) => {
      if (user.completed) {
        if (!dict[user.userId]) {
          dict[user.userId] = 1;
        } else {
          dict[user.userId] += 1;
        }
      }
    });
    console.log(dict);
  }
});
