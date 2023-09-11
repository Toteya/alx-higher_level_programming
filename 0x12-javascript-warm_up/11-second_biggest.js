#!/usr/bin/node

function findLargest (arr) {
  let largest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  return largest;
}

function findSecondLargest (arr) {
  const largest = findLargest(arr);
  let secondLargest;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < largest) {
      if (arr[i] > secondLargest || secondLargest === undefined) {
        secondLargest = arr[i];
      }
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
