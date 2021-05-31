#include <iostream>
#include <string>

using namespace std;

int main()
{
    int num;
    int total = 0;
    cin >> num;

    for (int i = 1 ; i <= num ; i++) {
        if (i < 100) {
            total += 1;
        } else {
            string tempStr = to_string(i);

            if (tempStr[1] - tempStr[0] == tempStr[2] - tempStr[1]) {
                total += 1;
            }
        }
    }

    cout << total << endl;

    return 0;
}