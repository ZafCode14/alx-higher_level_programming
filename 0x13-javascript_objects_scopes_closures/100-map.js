#!/usr/bin/node

const list = require('./100-data');
let i = 0;
const list2 = list.list.map((x) => x * i++);
console.log(list.list);
console.log(list2);
