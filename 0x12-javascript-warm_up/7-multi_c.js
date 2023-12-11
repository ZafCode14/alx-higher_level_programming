#!/usr/bin/node

const args = process.argv;
let number = parseInt(args[2], 10);

if (!isNaN(number)) {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
} else {
  console.log('Missing a number of occurrences');
}
