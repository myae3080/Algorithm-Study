// source : https://www.acmicpc.net/problem/30455

// input
const input = require('fs').readFileSync('example.txt').toString();

console.log(parseInt(input) % 2 ? 'Goose' : 'Duck');