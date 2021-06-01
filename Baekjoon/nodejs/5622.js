// String

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

// 기존의 map에 생으로 담아서 하는 방식 보다 느림.
dialList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'];

rl.on("line", (line) => {
    const input = line;
    let totalTime = 0;

    for (let i = 0; i < input.length; i++) {
        dialList.forEach((dial, idx) => {
            if(dial.includes(input[i])) {
                totalTime += (idx + 3);
            }
        });   
    }

    console.log(totalTime);

    rl.close();
}).on("close", () => {
  process.exit();
});
