// source : https://www.acmicpc.net/problem/31090

const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');

const years = input.slice(1);

for (year of years) {
    console.log(!((Number(year) + 1) % Number(year.substr(2, 2))) ? 'Good' : 'Bye');
}