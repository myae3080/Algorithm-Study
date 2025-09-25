// source : https://www.acmicpc.net/problem/19945

package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int

	// input
	fmt.Scan(&n)

	if n >= 0 {
		fmt.Println(len(strconv.FormatInt(int64(n), 2)))
	} else {
		fmt.Println(32)
	}
}