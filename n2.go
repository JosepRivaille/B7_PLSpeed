package main

import "fmt"
import "time"
import "math/rand"


func selection_sort(v []int) {
	for i := 0; i < 10000000; i++ {
		imin := i
		for j := i; j < 10000000; j++ {
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
	rand.Seed(time.Now().UTC().UnixNano())
	start := time.Now()
	v := make([]int, 10000000)
	for i:=0; i < 10000000; i++ {
		v[i] = rand.Intn(10000000)
	}
	selection_sort(v)
	fmt.Printf("--- %s ---\n", time.Since(start))
}