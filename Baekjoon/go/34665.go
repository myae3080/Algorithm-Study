// https://www.acmicpc.net/problem/34665

package main

import "fmt"

func main() {
	var A, B string

	fmt.Scanln(&A)
	fmt.Scanln(&B)

	if (A == B) {
		fmt.Println(0)
	} else {
		fmt.Println(1550)
	}
}