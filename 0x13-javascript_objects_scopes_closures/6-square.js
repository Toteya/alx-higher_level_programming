#!/usr/bin/node

const Square = require('./5-square');

class Square1 extends Square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
      return;
    }
    let squareLine = '';
    for (let i = 0; i < this.width; i++) {
      squareLine += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(squareLine);
    }
  }
}

module.exports = Square1;
