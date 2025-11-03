// source : https://www.acmicpc.net/problem/34543

package main

import "fmt"

func main() {
	var n, w int	

	// input
	fmt.Scanln(&n)
	fmt.Scanln(&w)

	var result = n * 10 
	if n >= 3 {
		result += 20
	}
	
	if n == 5 {
		result += 50
	}

	if w > 1000 {
		result -= 15
		if result < 0 {
			result = 0
		}
	}

	fmt.Println(result)
}