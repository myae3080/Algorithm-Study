// source : https://www.acmicpc.net/problem/14646

// input
const input: Array<string> = require('fs')
                            .readFileSync('example.txt')
                            .toString()
                            .trim()
                            .replace(/\r/g, "")
                            .split('\n');

const n: number = parseInt(input[0]);
const draw: Array<number> = input[1].split(' ').map(m => parseInt(m));

const menu: Array<Boolean> = Array.from({length: n + 1}, () => false);

let sticker: number = 0, result: number = 0;
for (let m of draw) {
    if (menu[m]) {
        sticker -= 1;
        menu[m] = false;
    } else {
        sticker += 1;
        menu[m] = true;
    }

    result = Math.max(result, sticker);
}

console.log(result);