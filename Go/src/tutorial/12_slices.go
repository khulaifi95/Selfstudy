package main

import "fmt"

func slices() {
	primes := [6]int {2, 3, 5, 7, 11, 13}

	var s []int = primes[1:4]	// [1, 4)
	fmt.Println(s)
}

func slice_pointers() {
	fmt.Println("\nPointers in slices:")

	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	// Slices don't save data but a reference to the array.
	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	// Change elements in slices change those in the array.
	b[0] = "XXX"
	fmt.Println(a, b)	// instant change to another slice
	fmt.Println(names)
}

func slice_literals() {
	fmt.Println("\nSlice literals:")

	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, false},
		{11, true},
		{13, true},
	}
	fmt.Println(s)
}

func slice_bounds() {
	p := []int{2, 3, 5, 7, 11, 13}

	p = p[1:4]
	fmt.Println(p)

	p = p[:2]
	fmt.Println(p)

	p = p[1:]
	fmt.Println(p)

	p = p[:]
	fmt.Println(p)
}


func main() {
	slices()
	slice_pointers()
	slice_literals()
	slice_bounds()
}