#!/usr/bin/node
exports.converter = function (base) {
return function convertToBase(number) {
return number === 0 ? '0' :
number < 0 ? '-' + convertToBase(-number):
convertToBase(Math.floor(number / base)) + (number % base).toString(base);
};
};
