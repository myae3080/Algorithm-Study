// source : https://www.acmicpc.net/problem/34400

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var t int

	// input
	fmt.Fscan(reader, &t)

	for i := 0; i < t; i++ {
		var time int

		// input
		fmt.Fscan(reader, &time)

		if (time % 25 < 17) {
			fmt.Println("ONLINE")
		} else {
			fmt.Println("OFFLINE")
		}
	}
}
