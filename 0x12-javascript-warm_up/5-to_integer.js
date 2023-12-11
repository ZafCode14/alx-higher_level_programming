#!/usr/bin/node

const args = process.argv;
const integer = parseInt(args[2], 10);

if (!isNaN(integer)) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
