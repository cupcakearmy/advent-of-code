package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type sRow struct {
	min, max       int
	char, password string
}

func parse(data []byte) []sRow {
	parsed := []sRow{}
	for _, row := range strings.Split(strings.TrimSpace(string(data)), "\n") {
		s0 := strings.Split(row, ":")
		rule := strings.TrimSpace(s0[0])
		password := strings.TrimSpace(s0[1])
		s1 := strings.Split(rule, " ")
		minMax := strings.TrimSpace(s1[0])
		char := strings.TrimSpace(s1[1])
		s2 := strings.Split(minMax, "-")
		min, _ := strconv.Atoi(strings.TrimSpace(s2[0]))
		max, _ := strconv.Atoi(strings.TrimSpace(s2[1]))

		r := sRow{
			min:      min,
			max:      max,
			char:     char,
			password: password,
		}
		parsed = append(parsed, r)
	}
	return parsed
}

func validSimple(rows []sRow) int {
	valid := 0
	for _, row := range rows {
		count := strings.Count(row.password, row.char)
		if row.min <= count && count <= row.max {
			valid++
		}
	}
	return valid
}

func validComplex(rows []sRow) int {
	valid := 0
	for _, row := range rows {
		l := len(row.password)
		min := row.min - 1
		max := row.max - 1
		if min >= l || max >= l {
			continue
		}
		r := []rune(row.password)
		a := string(r[min]) == row.char
		b := string(r[max]) == row.char
		if a != b {
			valid++
		}
	}

	return valid
}

func main() {
	data, _ := ioutil.ReadFile("./solutions/2/data.txt")
	rows := parse(data)
	simple := validSimple(rows)
	fmt.Println(simple)
	complex := validComplex(rows)
	fmt.Println(complex)
}
