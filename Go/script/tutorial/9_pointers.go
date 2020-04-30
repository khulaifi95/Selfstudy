// Pointer in Go saves the memory address of a value.

package main

import "fmt"

func main() {
	i, j := 42, 2701
	// & assigns the pointer to a value
	p := &i 		// set point to i
	
	// *T is the pointer that points to type T
	fmt.Println(*p)	// read i with pointer p

	// * represents the lower layer value of pointer
	*p = 21			// change i value with pointer p
	fmt.Println(i)	// read i value

	p = &j
	*p = *p / 37	// divide with pointer
	fmt.Println(j)
}