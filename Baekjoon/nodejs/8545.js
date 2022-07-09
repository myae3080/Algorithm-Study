// source : https://www.acmicpc.net/problem/8545
// string

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

rl.on("line", (line) => {
    console.log(line.split('').reverse().join(''))

    rl.close();
}).on("close", () => {
    process.exit();
});