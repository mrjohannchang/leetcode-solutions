// +build ignore

package main

import "fmt"
import "os"
import "strconv"

func getRow(rowIndex int) []int {
	row := make([]int, rowIndex+1)
	row[0] = 1
	for i := 0; i < rowIndex; i++ {
		for j := i; j > 0; j-- {
			row[j] = row[j] + row[j-1]
		}
		row[i+1] = 1
	}
	return row
}

func main() {
	k, _ := strconv.Atoi(os.Args[1])
	fmt.Println(getRow(k))
}
