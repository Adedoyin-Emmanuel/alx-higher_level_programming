#!/usr/bin/node
function nbOccurences (list, searchElement) {
  if (!list) return;
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      counter++;
    }
  }
  return counter;
}

module.exports = nbOccurences;
