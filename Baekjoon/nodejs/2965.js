// source : https://www.acmicpc.net/problem/2965
// math

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
});

let max = 0;

rl.on('line', (line) => {
    kangaroos = line.split(' ');

    console.log(Math.max(max, Number(kangaroos[1]) - Number(kangaroos[0]) - 1, Number(kangaroos[2]) - Number(kangaroos[1]) - 1));

    rl.close();
}).on('close', () => {
    process.exit();
});