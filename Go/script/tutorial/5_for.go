// Only one loop structure in Go: for

package main

import (
	"fmt"
)

func main() {
	sum := 0
	for i := 0; i < 10; i++ {	// short declaration before loop
		sum += i
	}
	fmt.Println(sum)

	for sum < 1000 {			// for -> while
		sum += sum
	}
	fmt.Println(sum)
	// for {
		// infinite loop
	// }
}