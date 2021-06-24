// string

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
});

let resultStrArray;

rl.on('line', (line) => {
    strArray = line.split('');

    resultStrArray = strArray.map(ch => {
        const asciiNum = ch.charCodeAt();
        let tempStr;

        // 대문자
        if (asciiNum >= 65 && asciiNum <= 90) {
            tempStr = String.fromCharCode(asciiNum + 32);
        } else {
            tempStr = String.fromCharCode(asciiNum - 32);
        }

        return tempStr;
    });

    console.log(resultStrArray.join(''));

    rl.close();
}).on('close', () => {
    process.exit();
});