package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const high = rune('#')

type sForest struct {
	data   [][]bool
	height int
	width  int
}

func (f sForest) at(y, x int) bool {
	if y >= f.height {
		return false
	}
	return f.data[y][x%f.width]
}

func (f sForest) traverse(y, x int) int {
	trees := 0
	for dy := 0; dy <= f.height; dy++ {
		tree := f.at(dy*y, dy*x)
		if tree {
			trees++
		}
	}
	return trees
}

func main() {
	data, _ := ioutil.ReadFile("./solutions/3/data.txt")

	rows := strings.Split(strings.TrimSpace(string(data)), "\n")
	height, width := len(rows), len(rows[0])
	d := make([][]bool, height)

	for y, row := range rows {
		d[y] = make([]bool, width)
		for x, char := range []rune(row) {
			d[y][x] = char == high
		}
	}

	forest := sForest{
		data:   d,
		height: height,
		width:  width,
	}

	fmt.Println("Simple: ", forest.traverse(1, 3))

	trees11 := forest.traverse(1, 1)
	trees13 := forest.traverse(1, 3)
	trees15 := forest.traverse(1, 5)
	trees17 := forest.traverse(1, 7)
	trees21 := forest.traverse(2, 1)

	fmt.Println(trees11, trees13, trees15, trees17, trees21)
	fmt.Println(trees11 * trees13 * trees15 * trees17 * trees21)

}
