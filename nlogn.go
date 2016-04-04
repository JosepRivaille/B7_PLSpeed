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
	rand.Seed(time.Now().UTC().UnixNano())
	start := time.Now()
	v := make([]int, 100000000)
	for i:=0; i < 100000000; i++ {
		v[i] = rand.Intn(100000000)
	}
	mergesort(v, 0, 99999999)
	fmt.Printf("--- %s ---\n", time.Since(start))
}