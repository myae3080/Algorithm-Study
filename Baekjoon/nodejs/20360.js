// source : https://www.acmicpc.net/problem/20360

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
});

rl.on("line", (line) => {
    // input
    const binary = Number(line).toString(2);

    console.log(
        [...binary]
            .reverse()
            .map((val, idx) => {
                if (val === "1") {
                    return idx;
                }
            })
            .filter((val) => val !== undefined)
            .join(" ")
    );

    rl.close();
}).on("close", () => {
    process.exit();
});
