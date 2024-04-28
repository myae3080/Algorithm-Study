// source : https://www.acmicpc.net/problem/27294

// input
const input: Array<string> = require('fs').readFileSync('example.txt').toString().trim().split(' ');

const [t, s] = input;

console.log((parseInt(t) >= 12 && parseInt(t) <= 16) && s === '0' ? 320 : 280);