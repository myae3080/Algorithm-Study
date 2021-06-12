// math, string

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
});

const octopusChar = {
    '-': 0,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}

resultList = [];

rl.on('line', (line) => {
    let total = 0;

    if (line === '#') {
        rl.close();
    }

    strArray = line.split('');

    strArray.forEach((ele, idx) => {
        const digit = strArray.length - idx - 1;
        // \ 문자는 key mapping이 까다로워서 해당 object에서 값을 찾지 못 하는 경우로 만들어 무조건 1을 리턴
        const matchNum = octopusChar[ele] === undefined ? 1 : octopusChar[ele];
        
        total += digit !== 0 ? matchNum * (8 ** digit) : matchNum;
    });

    console.log(total);
}).on('close', () => {
    process.exit();
});