// source : https://www.acmicpc.net/problem/17863

package main

import "fmt"

func main() {
	var input string

	// input
	fmt.Scanf("%s", &input)

	if input[:3] == "555" {
		fmt.Printf("YES")
	} else {
		fmt.Printf("NO")
	}
}