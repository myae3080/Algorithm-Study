#include <iostream>

using namespace std;

int main() {
    for (int i = 0; i < 3; i++) {
        int a, b, c, d, sum;

        // input
        cin >> a >> b >> c >> d;
        
        sum = a + b + c + d;

        switch(sum) {
            case 4:
                cout << 'E' << '\n';
                break;
            case 3:
                cout << 'A' << '\n';
                break;
            case 2:
                cout << 'B' << '\n';
                break;
            case 1:
                cout << 'C' << '\n';
                break;
            default:
                cout << 'D' << '\n';
                break;
        }
    }
}