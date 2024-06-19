#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return;
  };
  return function (number) {
    if (number === 0) {
      return '0';
    };

    let result = ' ';
    let n = Math.abs(number);

    while (n > 0) {
      const remainder = n % base;
      result = remainder.toString() + result;
      n = Math.floor(n / base);
    };

    if (number < 0) {
      result = '-' + result;
    };
    return result;
  };
};
