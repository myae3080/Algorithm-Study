// source : https://www.acmicpc.net/problem/26041

// input
const input: Array<string> = require('fs')
                            .readFileSync('example.txt')
                            .toString()
                            .trim()
                            .replace(/\r/g, "")
                            .split('\n');

const strs: Array<string> = input[0].split(' ');
const phoneNumber: string = input[1];

console.log(strs.filter((str) => str !== phoneNumber && str.indexOf(phoneNumber) === 0).length);