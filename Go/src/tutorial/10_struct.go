// A struct is a group of fields.

package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

var (
	v1 = Vertex{1, 2}
	v2 = Vertex{X: 1}	// Y:0
	v3 = Vertex{}		// X:0, Y:0
	p1  = &Vertex{1, 2}	// pointer to v1
)

func main() {
	v := Vertex{1, 2}
	fmt.Println(v)
	v.X = 4
	fmt.Println(v.X)
	// struct pointer
	p := &v 	// pointer to struct
	p.Y = 1e9	// hidden indirect reference
	fmt.Println(v)
	// struct syntax
	fmt.Println(v1, p1, v2, v3)	// &{} indicates a pointer to struct
}