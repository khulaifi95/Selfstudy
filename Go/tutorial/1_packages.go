package main

import (
	"fmt"
	"math"
	"math/rand"
)

func main() {
	fmt.Println("My favourite number is", rand.Intn(10))
	fmt.Println(math.Pi)	// pi -> unexported name
}
