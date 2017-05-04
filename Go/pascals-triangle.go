// +build ignore

package main

import "fmt"
import "os"
import "strconv"

func generate(numRows int) [][]int {
	ret := [][]int{}

	if numRows < 1 {
		return ret
	}

	row := []int{1}
	ret = append(ret, row)

	for i := 1; i < numRows; i++ {
		row := make([]int, i+1)
		prevRow := ret[i-1]
		row[0], row[i] = 1, 1
		for j := 1; j < i; j++ {
			row[j] = prevRow[j] + prevRow[j-1]
		}
		ret = append(ret, row)
	}

	return ret
}

func main() {
	k, _ := strconv.Atoi(os.Args[1])
	fmt.Println(generate(k))
}
