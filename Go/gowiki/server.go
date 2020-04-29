// +build ignore

package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r * http.Request) {
	fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])	// drop "/"
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}