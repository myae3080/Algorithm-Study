// source : https://www.acmicpc.net/problem/17256

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

const input = [];

rl.on('line', (line) => {
    // input
    input.push(line);

    if (input.length === 2) {
        a = input[0].split(' ').map((num) => Number(num));
        c = input[1].split(' ').map((num) => Number(num));
        
        console.log(c[0] - a[2], c[1] / a[1], c[2] - a[0]);
    }

    input.length === 2 && rl.close();
}).on('close', () => {
    process.exit();
});