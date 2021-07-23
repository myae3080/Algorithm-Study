// math, string, sorting, number theory

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// sorting 내림차순
bool compare(int a, int b) {
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<int> numVector;
    string inputNum;
    int sum;

    // input
    cin >> inputNum;

    int strLength = inputNum.length();

    for (int i = 0; i < strLength; i++) {
        int tempNum = inputNum[i] - '0';

        numVector.push_back(tempNum);
        sum += tempNum;
    }

    // sorting
    sort(numVector.begin(), numVector.end(), compare);

    // python 처럼 vector[-1] 사용 시 전혀 다른 값이 나옴.
    if (sum % 3 != 0 || numVector[strLength - 1] != 0) {
        cout << -1;
    } else {
        for (int n : numVector) {
            cout << n;
        }
    }

    return 0;
}