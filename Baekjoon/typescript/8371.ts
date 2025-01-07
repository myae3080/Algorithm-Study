// source : https://www.acmicpc.net/problem/8371

// input
const input: Array<string> = require('fs').readFileSync('example.txt').toString().replace(/\r/g, "").split('\n');

const [n, a, b] = input;

let result = 0;
for (let i = 0; i < Number(n); i++) {
    if (a[i] !== b[i]) {
        result++;
    }
}

console.log(result);