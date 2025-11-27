// source : https://www.acmicpc.net/problem/25814

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var strNum1, strNum2 string
	
	// input
	fmt.Fscan(reader, &strNum1, &strNum2)

	weight1 := 0
	for _, c := range strNum1 {
		weight1 += int(c - '0')
	}
	weight1 *= len(strNum1)

	weight2 := 0
	for _, c := range strNum2 {
		weight2 += int(c - '0')
	}
	weight2 *= len(strNum2)

	if (weight1 > weight2) {
		fmt.Println("1")
	} else if (weight1 < weight2) {
		fmt.Println("2")
	} else {
		fmt.Println("0")
	}
}