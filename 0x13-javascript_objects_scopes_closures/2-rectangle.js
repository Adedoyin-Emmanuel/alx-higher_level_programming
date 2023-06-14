#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((parseInt(w) === 0 || parseInt(h) === 0) || (parseInt(w) < 0 || parseInt(h) < 0)) {
      return;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
