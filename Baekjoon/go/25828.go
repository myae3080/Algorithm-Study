// https://www.acmicpc.net/problem/25828

package main

import (
	"fmt"
)

func main() {
	var g, p, t int

	// input
	fmt.Scan(&g, &p, &t)

	individual := g * p
	group := g + p * t

	if individual > group {
		fmt.Println(2)
	} else if individual < group {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}