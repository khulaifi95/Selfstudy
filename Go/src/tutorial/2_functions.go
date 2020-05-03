package main

import (
	"fmt"
)

// function declaration
func add(x, y int) int {	// omit same type
	return x + y
}

// function with multiple results
func swap(x, y string) (string, string) {
	return y, x
}

// named return values
func split(sum int) (x, y int) {	// treated as variables
	x = sum * 4 / 9
	y = sum - x
	return    // naked return
}

func main() {
	fmt.Println(add(18, 42))
	fmt.Println(swap("help", "me"))
	fmt.Println(split(21))
}