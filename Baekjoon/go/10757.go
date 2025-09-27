// source : https://www.acmicpc.net/problem/10757

package main

import (
	"bufio"
	"fmt"
	"os"
	"math/big"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	var A, B string
	
	// input
	fmt.Fscan(reader, &A, &B)

	a := new(big.Int)
	b := new(big.Int)

	a.SetString(A, 10)
	b.SetString(B, 10)

	fmt.Println(new(big.Int).Add(a, b))
}