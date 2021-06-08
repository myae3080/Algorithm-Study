// math

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin
});

rl.on("line", (line) => {
    const input = line.split(' ').map(num => BigInt(num));

    console.log((input[0] + input[1]).toString());

    /*
    입력 받을 때, BigInt형으로 받지 않고 string으로 받아 후에 BigInt로 변환 후 더해서 결과를 출력했을 때, 통과되지 않음.
    두 경우의 차이점은 아직 명확히 모르겠음.
    숫자 관련 문제는 고통받지 말고 python으로 해결하자.

    const input = line;

    console.log((BigInt(input[0]) + BigInt(input[1])).toString());
    */

    rl.close();
}).on("close", () => {
    process.exit();
});
