#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const firstArg = parseInt(process.argv[2]);
if (isNaN(firstArg)) {
  console.log('1');
} else {
  console.log(factorial(firstArg));
}
