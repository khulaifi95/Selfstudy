package main

import (
	"fmt"
	"strings"
)

func slices_of_slice() {	// two dimensional matrix
	// create a # board
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

func append_slices() {
	var s []int
	printSlice(s)	// 0 0 []

	s = append(s, 0)	// append a nil slice
	printSlice(s)	// 0 0 [0]

	s = append(s, 1)	// slice grows as needed
	printSlice(s)	// 1 1 [0, 1]

	s = append(s, 2, 3) // appending multiple elements
	printSlice(s)	// 3 3 [0, 1, 2, 3]
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
	slices_of_slice()
	append_slices()
}