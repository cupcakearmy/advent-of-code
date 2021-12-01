package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const target uint64 = 2020

func findTwo(list []uint64) {
	for _, a := range list {
		for _, b := range list {
			if a+b == target {
				fmt.Printf("The numbers: %v and %v.\tSolution: %v\n", a, b, a*b)
				return
			}
		}

	}
}

func findThree(list []uint64) {
	for _, a := range list {
		for _, b := range list {
			for _, c := range list {
				if a+b+c == target {
					fmt.Printf("The numbers: %v, %v and %v.\tSolution: %v\n", a, b, c, a*b*c)
					return
				}
			}
		}
	}
}

func main() {
	data, err := ioutil.ReadFile("./solutions/1/data.txt")
	if err != nil {
		fmt.Println("File reading error", err)
		return
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	intLines := []uint64{}
	for _, i := range lines {
		num, _ := strconv.ParseUint(i, 10, 64)
		intLines = append(intLines, num)
	}

	// fmt.Println("Result: ", findTwo(intLines))
	// fmt.Println("Result: ", findThree(intLines))
	findTwo(intLines)
	findThree(intLines)
}
