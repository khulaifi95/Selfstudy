package main

import (
	"fmt"
)

// var c, python, java bool
var c, python, java = true, false, "no!"	// type omitted

func main() {
	// var i int
	var i, j = 1, 2
	k := 3	// short declaration inside function only
	// with implicit type
	fmt.Println(i, j, k, c, python, java)
}