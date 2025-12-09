// source : https://www.acmicpc.net/problem/26742

package main

import (
	"fmt"
)

func main() {
	var socks string

	// input
	fmt.Scan(&socks)

	var bCnt, cCnt int
	for i := 0; i < len(socks); i++ {
        if socks[i] == 'B' {
			bCnt++
		} else {
			cCnt++
		}
    }

	fmt.Println(bCnt / 2 + cCnt / 2)
}