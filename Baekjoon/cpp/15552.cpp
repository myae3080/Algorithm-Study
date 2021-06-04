// fast io

#include <iostream>
using namespace std;

int main(void) {
    int count, num1, num2 = 0;

    // deactivate sync between iostream and stdio
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> count;
	
	for(int i = 0; i < count; i++) {
		cin >> num1 >> num2;
		cout << num1 + num2 << '\n';
	}    
    
    return 0;
}