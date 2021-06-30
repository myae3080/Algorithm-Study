// math

#include <iostream>

using namespace std;

int main() {
    int n, m;
    int totalScore = 0;
    int temp = 0;

    // input
    cin >> n;

    for (int i = 0; i < n; i++) {
        // input
        cin >> m;

        if (m == 1) {
            temp += m;
            totalScore += temp;
        } else {
            temp = 0;
        }
    }

    cout << totalScore << "\n";

    return 0;
}