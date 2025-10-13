// source : https://www.acmicpc.net/problem/9924

package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b float64

	// input
	fmt.Scan(&a, &b)

	var result int
	for a != b {
		result++

		a, b = math.Min(a, b), math.Abs(a - b)
		
		if a == b {
			break
		}

	}
	
	fmt.Println(result)
}