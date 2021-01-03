package main

import "fmt"

func count() {
	fmt.Println("Counting...")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)	// deferred function pushed into a LIFO stack
	}

	fmt.Println("Done.")
}

func main() {	
	defer fmt.Println("world")	// evaluated but deferred until outer return
	fmt.Println("hello")
	count()
}

