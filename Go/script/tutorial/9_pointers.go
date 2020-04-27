// Pointer in Go saves the memory address of a value.

package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i 		// set point to i
	fmt.Println(*p)	// read i with pointer p
	*p = 21			// change i value with pointer p
	fmt.Println(i)	// read i value

	p = &j
	*p = *p / 37	// divide with pointer
	fmt.Println(j)
}