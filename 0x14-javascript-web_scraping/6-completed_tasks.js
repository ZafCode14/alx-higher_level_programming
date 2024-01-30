#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const data = JSON.parse(body);
    const dict = {};
    let count = 0;
    let usersId = 0;
    data.forEach((user) => {
      if (usersId !== user.userId) {
        count = 0;
        usersId = user.userId;
      }
      if (user.completed === true) {
        count++;
      }
      dict[user.userId] = count;
    });
    console.log(dict);
  }
});
