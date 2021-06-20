// math

#include <iostream>

using namespace std;

int main() {
    int n;
    int apple = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int a, b;

        cin >> a >> b;

        apple += (b % a);
    }

    cout << apple;

    return 0;
}