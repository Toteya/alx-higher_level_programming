#!/usr/bin/node

function findSecondLargest (arr) {
  let largest = arr[0];
  let secondLargest;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    } else if (arr[i] > secondLargest || secondLargest === undefined) {
      secondLargest = arr[i];
    }
  }
  if (secondLargest === undefined) {
    return 0;
  }
  return secondLargest;
}

const process = require('process');
const myArray = process.argv.slice(2);
for (const i in myArray) {
  myArray[i] = parseInt(myArray[i]);
}
console.log(findSecondLargest(myArray));
