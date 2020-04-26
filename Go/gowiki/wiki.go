package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

// data structures
type Page struct {
	Title string
	Body  []byte  // a byte slice; for io usage
}

// save method
// This is a method that takes as its receiver p, a pointer to Page.
// It takes no parameters, and returns a value of type error.

func (p *Page) save() error {	// return nil if all goes well
	filename := p.Title + ".txt"
	return ioutil.WriteFile(filename, p.Body, 0600)	// current user only
}

// load method
func loadPage(title string) (*Page, error) {
	filename := title + ".txt"
	body, err := ioutil.ReadFile(filename)  // []byte, error
	if err != nil {	 // check if the page does not exist
		return nil, err
	}
	return &Page{Title: title, Body: body}, nil
}

// view handler
func viewHandler(w http.ResponseWriter, r *http.Request) {
	title := r.URL.Path[len("/view/"):]
	p, _ := loadPage(title)
	fmt.Fprintf(w, "<h1>%s</h1><div>%s</div>", p.Title, p.Body)
}


func main() {
	p1 := &Page{Title: "TestPage", Body: []byte("Sample page.")}
	p1.save()
	p2, _ := loadPage("TestPage")
	fmt.Println(string(p2.Body))
}