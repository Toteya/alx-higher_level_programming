#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let i = 0; i < list.length; i++) {
    reverseList[i] = list[list.length - (i + 1)];
  }
  return reverseList;
};
