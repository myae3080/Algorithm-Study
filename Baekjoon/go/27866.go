// source : https://www.acmicpc.net/problem/27866

package main

import "fmt"

func main() {
	var word string
	var idx int

	// input
	fmt.Scanln(&word)
	fmt.Scanln(&idx)

	fmt.Printf("%c", word[idx-1])
}
