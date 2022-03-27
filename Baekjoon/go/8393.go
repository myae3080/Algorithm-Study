// source : https://www.acmicpc.net/problem/8393

package main

import "fmt"

func main() {
	var n int
	var sum int

	fmt.Scanf("%d", &n)

	for i := 1; i <= n; i++ {
		sum += i
	}

	fmt.Printf("%d", sum)
}
