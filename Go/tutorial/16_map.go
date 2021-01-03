package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40, -74,
	},
	"Google": {37.42202, -122.08408},	
	// leave out the type name 
	"Apple": {37.2005, 122.0032},
}

func main() {
	m["Bell Labs"] = Vertex{	// edit an element 
		40.68433, -74.39967,
	}
	delete(m, "Apple")			// delete an element

	v, exist := m["Apple"]		// double return to check an element
	fmt.Println("Value:", v, "Present?", exist)

	fmt.Println(m)
}