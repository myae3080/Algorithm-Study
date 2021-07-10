// star

#include <iostream>

using namespace std;

int main() {
    int n;

    // input
    cin >> n;

    if (n == 1) {
        cout << '*';
    } else {
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < n; j++) {
                    cout << "* ";
                }

                cout << "\n";
            } else {
                for (int j = 0; j < n; j++) {
                    cout << " *";
                }

                cout << "\n";
            }
        }
    }

    return 0;
}