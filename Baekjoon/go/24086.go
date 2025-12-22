// source : https://www.acmicpc.net/problem/24086

package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b int

	// input
	fmt.Scan(&a, &b)

	fmt.Println(math.Abs(float64(a - b)))
}