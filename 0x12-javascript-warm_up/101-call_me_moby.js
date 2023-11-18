#!/usr/bin/node

exports.callMeMoby = function (x, thefunc) {
  for (let i = 0; i < x; i++) thefunc();
};
