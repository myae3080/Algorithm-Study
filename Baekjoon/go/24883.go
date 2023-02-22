// source : https://www.acmicpc.net/problem/24883

package main

import "fmt"

func main() {
	var input string

	// input
	fmt.Scanf("%s", &input)

	if input == "N" || input == "n" {
		fmt.Printf("Naver D2")
	} else {
		fmt.Printf("Naver Whale")
	}
}
