// source : https://www.acmicpc.net/problem/5358

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

const repl = {'i': 'e', 'e': 'i', 'I': 'E', 'E': 'I'};

rl.on('line', (line) => {
    try {
        // input
        console.log(line.split('').map((c) => c in repl ? repl[c] : c).join(''));
    } catch(e) {
        rl.close();
    }
}).on('close', () => {
    process.exit();
});