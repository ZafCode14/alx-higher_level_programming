#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[j] = list[i];
    j++;
  }
  return (newList);
};
