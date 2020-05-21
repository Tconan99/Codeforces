// https://codeforces.com/contest/1353/problem/C

package main

import (
	"fmt"
	"os"
)

func main() {

	f, err := os.Open("./file/input.txt")
	if err != nil {
		fmt.Println("2")
	} else {
		fmt.Println("1")
	}

	if f != nil {
		fmt.Println("3")
	} else {
		fmt.Println(4)
	}

	defer f.Close()

	oldStdin := os.Stdin
	defer func() {
		os.Stdin = oldStdin
	}()

	if err == nil {
		// os.Stdin = f
	}

	var t, n, result, k int64

	fmt.Scanln(&t)
	for ; t > 0; t-- {
		fmt.Scanln(&n)
		result = 0
		for k = 1; k <= n/2; k++ {
			result += 4 * k * 2 * k
		}
		fmt.Println(result)
	}
}
