// source : https://www.acmicpc.net/problem/27106

package main

import (
	"fmt"
)

func main() {
	var p int

	// input
	fmt.Scan(&p)

	var coins [4]int = [4]int{25, 10, 5, 1}
	var result [4]int = [4]int{0, 0, 0, 0}

	var change int = 100 - p
	for i := 0; i < 4; i++ {
		if change >= coins[i] {
			result[i] = change / coins[i]
			change = change % coins[i]
		}
	}
	
	fmt.Println(result[0], result[1], result[2], result[3])
}