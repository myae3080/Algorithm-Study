// source : https://www.acmicpc.net/submit/30501

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

const input = [];

rl.on('line', (line) => {
    // input
    input.push(line);
    
    if ((input.length - 1) === Number(input[0])) {
        result = input.slice(1).filter((name) => name.includes('S'));

        console.log(result[0]);
    }

    (input.length - 1) === Number(input[0]) && rl.close();
}).on('close', () => {
    process.exit();
});