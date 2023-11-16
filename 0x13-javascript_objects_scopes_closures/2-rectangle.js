#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (typeof wifth === 'number' && typeof height === 'number' && width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }
}
module.exports = Rectangle;
