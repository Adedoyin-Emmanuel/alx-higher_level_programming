#!/usr/bin/node
const argumentLength = process.argv.length;
const firstArgument = parseInt(process.argv[2]);
if (argumentLength < 3) {
  console.log('Not a number');
} else if (argumentLength === 3) {
  console.log(firstArgument);
}
