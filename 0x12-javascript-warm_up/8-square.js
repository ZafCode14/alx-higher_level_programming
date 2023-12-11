#!/usr/bin/node

const args = process.argv;
let number = parseInt(args[2], 10);
const j = number;

if (!isNaN(number)) {
  while (number > 0) {
    let string = '';
    for (let i = j; i > 0; i--) {
      string += 'X';
    }
    console.log(string);
    number--;
  }
} else {
  console.log('Missing size');
}
