// source : https://www.acmicpc.net/problem/30684

// input
const input: Array<string> = require('fs').readFileSync('example.txt').toString().replace(/\r/g, "").split('\n');

const names = input.slice(1);

console.log(names.filter((name) => name.length === 3).sort()[0]);