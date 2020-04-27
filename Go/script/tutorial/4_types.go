package main

import (
	"fmt"
	"math/cmplx"
	"math"
)

// factored declaration
var (	
	ToBe bool = false
	MaxInt uint64 = 1<<64 - 1
	z complex128 = cmplx.Sqrt(-5 + 12i)
)

// uninitiated variables set to 0
var (	
	i int
	f float64
	b bool
	s string
	c complex128
)

// type conversions
func changeType(x, y int) uint {
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	return z
}

// constants
const Pi = 3.14
const World = "世界"

// numeric constants
const (
	Big = 1 << 100	// shift 1 bit left 100 digits
	Small = Big >> 99	// shift it right 99 digits
)

func needInt(x int) int { return x*10 + 1}
func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
	fmt.Printf("%v %v %v %v %q\n", i, f, b, c, s)
	fmt.Println(changeType(3, 4))
	v := 42	// type inference
	fmt.Printf("v is of type %T\n", v)
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
	// fmt.Println(needInt(Big))	// overflow
}
