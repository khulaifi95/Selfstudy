package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func fibonacci() func() int {
    first, second := 0, 1
    return func() int {
        ret := first
        first, second = second, first+second
        return ret
    }
}

func main() {
	pos, neg := adder(), adder()
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(pos(i), neg(-2*i), f())
	}
}

