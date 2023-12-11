#!/usr/bin/node

const args = process.argv;
const num = parseInt(args[2], 10);

function factorialRecursion (n) {
  if (n === 0 || n === 1 || !n) {
    return (1);
  } else {
    return (n * factorialRecursion(n - 1));
  }
}
console.log(factorialRecursion(num));
