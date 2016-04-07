package main

import "fmt"
import "time"
import "math/rand"


func selection_sort(v []int, size int) {
	for i := 0; i < size; i++ {
		imin := i
		for j := i; j < size; j++ {
			if v[j] < v[imin] {
				imin = j;
			} 
		}
		if imin != i {
			aux := v[i]
			v[i] = v[imin]
			v[imin] = aux
		}
	}
}

func main() {
	var size int
	fmt.Printf("Write vector size: ")
	fmt.Scan(&size)
	v := make([]int, size)
	for i:=0; i < size; i++ {
		v[i] = rand.Intn(size)
	}
	rand.Seed(time.Now().UTC().UnixNano())
	start := time.Now()
	selection_sort(v, size)
	fmt.Printf("--- %s ---\n", time.Since(start))
}