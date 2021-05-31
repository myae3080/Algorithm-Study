// function

const nonSelfNumberArray = [];

const getNonSelfNumber = (num) => {
    let resultNum;
    
    if (num >= 1000) {
        resultNum = num + (parseInt(num / 1000)) + (parseInt((num % 1000) / 100)) + (parseInt((num % 100) / 10)) + (num % 10) ;
    } else if (num >= 100) {
        resultNum = num + (parseInt(num / 100)) + (parseInt((num % 100) / 10)) + (num % 10);
    } else if (num >= 10) {
        resultNum = num + (parseInt(num / 10)) + (num % 10) ;
    } else {
        resultNum = num * 2;
    }

    return resultNum;
}

// i의 순서대로 크기가 증가하는 패턴이 아님!
for (let i = 1; i <= 10000; i++) {
    const tempNum = getNonSelfNumber(i);

    if (tempNum <= 10000) {
        nonSelfNumberArray.push(tempNum);
    }
}

for (let i = 1; i <= 10000; i++) {
    (!nonSelfNumberArray.includes(i)) && console.log(i);
}