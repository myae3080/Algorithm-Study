// source : https://www.acmicpc.net/problem/13222

// input
const input = require('fs')
                .readFileSync('example.txt')
                .toString()
                .trim()
                .replace(/\r/g, "")
                .split('\n');

const [rest, ...nums] = input;
const [n, w, h] = rest.split(' ');

nums.forEach(num => num ** 2 <= (w ** 2) + (h ** 2) ? console.log('YES') : console.log('NO'));