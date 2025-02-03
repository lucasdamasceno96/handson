package main

import (
	"fmt"
	"net/http"
	"os"
)

func handler(w http.ResponseWriter, r *http.Request) {
	var name,_ = os.Hostname()
	fmt.Fprintf(w, "The server is running on %s\n", name)
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Fprintf(os.Stdout, "Starting server on port 8080\n")
	http.ListenAndServe(":8080", nil)
}