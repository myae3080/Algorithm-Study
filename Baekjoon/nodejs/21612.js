// source : https://www.acmicpc.net/submit/21612

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

rl.on('line', (line) => {
    // input
    const temperature = Number(line);

    const paskal = 5 * temperature - 400;

    console.log(paskal);
    console.log(paskal > 100 ? -1 : paskal === 100 ? 0 : 1);

    rl.close();
}).on('close', () => {
    process.exit();
});