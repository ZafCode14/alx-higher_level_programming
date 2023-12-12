#!/usr/bin/node

const fs = require('fs');

function concat (fileA, fileB, fileC) {
  const data1 = fs.readFileSync(fileA, 'utf8');
  const data2 = fs.readFileSync(fileB, 'utf8');
  const data3 = data1 + data2;

  fs.writeFileSync(fileC, data3);
}

const args = process.argv.slice(2);

concat(args[0], args[1], args[2]);
