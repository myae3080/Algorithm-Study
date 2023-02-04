// source : https://www.acmicpc.net/problem/17863

package main

import "fmt"

func main() {
	var input string

	// input
	fmt.Scanf("%s", &input)

	var strFive = "5"

	if string(input[0]) == strFive && string(input[1]) == strFive && string(input[2]) == strFive {
		fmt.Printf("YES")
	} else {
		fmt.Printf("NO")
	}
}