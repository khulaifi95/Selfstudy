package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {	// no need for ( )
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	return lim	// undefined if 'v'
}

func newtonSqrt(x float64) float64 {
	z := 1.0	// float
	// for i := 0; i < 10; i++ {
	for math.Abs(z*z - x) >= 1e-7 {
		z -= (z*z - x) / (2*z)
	}
	return z
}

func main() {
	fmt.Println(sqrt(2), sqrt(-4))
	fmt.Println(pow(3, 2, 10), pow(3, 3, 20))
	fmt.Println(newtonSqrt(2), newtonSqrt(3))
}