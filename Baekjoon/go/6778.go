// source : https://www.acmicpc.net/problem/6778

package main

import "fmt"

func main() {
	var antenna int
	var eyes int

	// input
	fmt.Scanln(&antenna)
	fmt.Scanln(&eyes)

	if antenna >= 3 && eyes <= 4 {
		fmt.Println("TroyMartian")
	}

	if antenna <= 6 && eyes >= 2 {
		fmt.Println("VladSaturnian")
	}

	if antenna <= 2 && eyes <= 3 {
		fmt.Println("GraemeMercurian")
	}
}
