// source : https://www.acmicpc.net/problem/25372

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// input
const input = [];
rl.on('line', (line) => {
    input.push(line);
});

rl.on('close', () => {
    input.slice(1).forEach((pw) => {(pw.length >= 6 && pw.length <= 9) ? console.log('yes') : console.log('no')});
    
    process.exit();
})