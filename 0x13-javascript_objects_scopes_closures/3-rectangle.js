#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (
      parseInt(w) === 0 ||
      parseInt(h) === 0 ||
      parseInt(w) < 0 ||
      parseInt(h) < 0
    ) {
      return;
    }
    this.width = w;
    this.height = h;
    
    this.print = () =>{
        for (let i = 0; i < this.width; i++){
          let row = '';
          for (let j = 0; i < this.height;  j++){
           row += 'X';
          }
          console.log(row);
        }
    }
  }
}
module.exports = Rectangle;
