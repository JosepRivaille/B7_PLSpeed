package main

import "fmt"
import "time"
import "math/rand"


func merge(v []int, e int, m int, d int) {
	size := d-e+1
	B := make([]int, size)
	i := e
	j := m + 1
	k := 0
	for i <= m && j <= d {
		if v[i] <= v[j] {
			B[k] = v[i]
			k++
			i++
		} else {
			B[k] = v[j]
			k++
			j++
		}
	}
	for i <= m {
		B[k] = v[i]
		k++
		i++
	}
	for j <= d {
		B[k] = v[j]
		k++
		j++
	}
	for k := 0; k <= d-e; k++ {
		v[e+k] = B[k]
	}	
}

func mergesort(v []int, e int, d int) {
	if e < d {
		m := (e+d)/2
		mergesort(v, e, m)
		mergesort(v, m+1, d)
		merge(v, e, m, d)
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
	mergesort(v, 0, size - 1)
	fmt.Printf("--- %s ---\n", time.Since(start))
}