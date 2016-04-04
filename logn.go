package main

import "fmt"
import "time"

func b_search(v[10000000] int, x int, l int, r int) int {
	for l<=r {
		m := (l+r)/2
		if v[m] == x {
			return m
		} else if v[m] < x {
			l = m+1
		} else {
			r =  m-1
		}
	}
	return -1
}

func main() {
	start := time.Now()
	var v [10000000] int
	for i:=0; i < 10000000; i++ {
		v[i] = i
	}
	x := 30
	b_search(v, x, 0, 9999999)
	fmt.Printf("--- %s ---\n", time.Since(start))
}