#include <iostream>
#include <cmath>

using namespace std;

int main() {
    /* 
        두 번째 풀이
    */
    int inputNum;
    cin >> inputNum;

    int colNum = 1;

    while (inputNum > colNum) {
        inputNum -= colNum;
        colNum++;
    }

    (colNum % 2 == 0) ? (cout << inputNum << "/" << (colNum + 1) - inputNum) : (cout << (colNum + 1) - inputNum << "/" << inputNum);

    /* 
        첫 번째 풀이
    */
    int inputNum;
    cin >> inputNum;

    int baseNum = 0;
    int numerator = 0;
    int denominator = 0;
    int colNum = 0;

    for (int i = 1; i <= inputNum; i++) {
        if((pow(i, 2) + i) >= 2 * inputNum) {
            colNum = i;
            denominator = i;
            numerator = 1;

            if (colNum % 2 == 1) {
                baseNum = (pow(i, 2) + i) / 2;
            } else {
                baseNum = ((pow(i - 1, 2) + i - 1) / 2) + 1;
            }

            break;
        }
    }

    if (!(baseNum == inputNum)) {
        if (colNum % 2 == 1) {
            for (int i = inputNum; i < baseNum; i++) {
                denominator -= 1;
                numerator += 1;
            }
        } else {
            for (int i = baseNum; i < inputNum; i++) {
                denominator -= 1;
                numerator += 1;
            }
        }
    }

    cout << numerator << "/" << denominator << endl;
}