package main

import(
		"fmt"
    "io"
		"os"
)

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

func readFile(filePath string) (numbers []int) {
    fd, err := os.Open(filePath)
    if err != nil {
        panic(fmt.Sprintf("open %s: %v", filePath, err))
    }
    var line int
    for {

        _, err := fmt.Fscanf(fd, "%d\n", &line)

        if err != nil {
            fmt.Println(err)
            if err == io.EOF {
                return
            }
            panic(fmt.Sprintf("Scan Failed %s: %v", filePath, err))

        }
        numbers = append(numbers, line)
    }
    return
}

func main() {
	filename := os.Args[2]
	v := readFile(filename)
	mergesort(v, 0, len(v) - 1)
	//for i := 0; i < len(v); i++ {
	//	fmt.Printf("%d\n", v[i])
	//}
}
