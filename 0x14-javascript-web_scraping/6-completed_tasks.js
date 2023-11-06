#!/usr/bin/node
// Computes the number of tasks completed bu user id

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);
  const todos = JSON.parse(body);
  const dict = {};

  for (const todo of todos) {
    if (!todo.completed) continue;

    if (todo.userId in dict) {
      dict[todo.userId.toString()]++;
    } else {
      dict[todo.userId.toString()] = 1;
    }
  }
  console.log(dict);
});
