// fast io

#include <iostream>

int main(void) {
    int count, num1, num2 = 0;

    // deactivate sync between iostream and stdio
	std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
	std::cin >> count;
	
	for(int i = 0; i < count; i++) {
		std::cin >> num1 >> num2;
		std::cout << num1 + num2 << '\n';
	}    
    
    return 0;
}