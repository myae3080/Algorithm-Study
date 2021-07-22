// sorting

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int numArray[3];

    for (int i = 0; i < 3; i++) {
        // input
        cin >> numArray[i];
    }

    sort(numArray, numArray + 3);

    for (int i = 0; i < 3; i++) {
        cout << numArray[i] << ' ';
    }

    return 0;
}