// source : https://www.acmicpc.net/problem/20976

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"sort"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	// input
	line := scanner.Text()

	strNums := strings.Fields(line)
	nums := make([]int, len(strNums))
	for i, s := range strNums {
		nums[i], _ = strconv.Atoi(s)
	}

	sort.Ints(nums)

	fmt.Println(nums[len(nums) / 2])
}