// math

#include <iostream>

using namespace std;

int main() {
    int price, n, money, total;

    cin >> price >> n >> money;

    total = price * n;

    if (total > money) {
        cout << total - money;
    } else {
        cout << 0;
    }
}