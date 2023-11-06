#!/usr/bin/node
// Computes the number of tasks completed bu user id

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);
  const todos = JSON.parse(body);
  let id = 0;
  let tasksCompleted = 0;
  const dict = {};

  for (const todo of todos) {
    if (todo.userId !== id) {
      if (tasksCompleted !== 0) dict[id.toString()] = tasksCompleted;
      id = todo.userId;
      tasksCompleted = 0;
    }
    if (todo.completed) {
      tasksCompleted++;
    }
  }
  if (tasksCompleted !== 0) dict[id.toString()] = tasksCompleted;
  console.log(dict);
});
