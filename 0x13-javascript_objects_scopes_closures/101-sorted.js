#!/usr/bin/node

const dict = require('./101-data').dict;
const dict2 = {};

for (const key in dict) {
  dict2[dict[key]] = [];
}
for (const key in dict) {
  dict2[dict[key]].push(key);
}
console.log(dict2);
