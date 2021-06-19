const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

let input = [];

rl.on('line', (line) => {
    input.push(line);

    if (input.length === 2) {
        day = input[0];
        carArray = input[1].split(' ');

        console.log(carArray.filter(ele => ele === day).length);
    }

    input.length === 2 && rl.close();
}).on('close', () => {
    process.exit();
});