#!/usr/bin/node
let firstArgument = process.argv[3];
let secondArgument = process.argv[4];
const arg = process.argv;

if (!arg[2]) {
  firstArgument = 'undefined';
  secondArgument = 'undefined';
} else if (!arg[3]) {
  firstArgument = arg[2];
  secondArgument = 'undefined';
} else {
  firstArgument = arg[2];
  secondArgument = arg[3];
}

console.log(firstArgument + ' is ' + secondArgument);
