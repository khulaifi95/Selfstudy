package main

import "fmt"

func slice_len_cap() {
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	s = s[:0]	// length -> 0
	printSlice(s)

	s = s[:4]
	printSlice(s)

	s = s[2:]	// reduce both len and cap
	printSlice(s)
}

func nil_slices() {
	var s []int
	fmt.Println(s, len(s), cap(s))	// length and capacity
	if s == nil {
		fmt.Println("nil!")
	}
}

func make_slices() {
	a := make([]int, 5)
	fmt.Println("a:")
	printSlice(a)

	b := make([]int, 0, 5)	// capacity -> 5
	fmt.Println("b:")
	printSlice(b)	// [] because len(b) = 0

	c := b[:2]
	fmt.Println("c:")
	printSlice(c)	// referencing the original array of b

	d := c[2:5]
	fmt.Println("d:")
	printSlice(d)	// still a reference to b

}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
	slice_len_cap()
	nil_slices()
	make_slices()
}