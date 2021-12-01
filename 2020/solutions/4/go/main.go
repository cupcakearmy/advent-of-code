package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"

	k "github.com/wesovilabs/koazee"
)

type tPassport = map[string]string

func stringBetween(s string, min, max int) bool {
	num, _ := strconv.Atoi(s)
	return min <= num && num <= max
}

func verifyPassport(passport tPassport) (bool, bool) {
	requiredKeys := k.StreamOf([]string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"})
	eyeColors := k.StreamOf([]string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})

	// Simple
	counted := 0
	for k := range passport {
		if k == "cid" {
			continue
		}
		included, _ := requiredKeys.Contains(k)
		if !included {
			return false, false
		}
		counted++
	}
	if counted < 7 {
		return false, false
	}

	// Complex
	if !stringBetween(passport["byr"], 1920, 2002) || !stringBetween(passport["iyr"], 2010, 2020) || !stringBetween(passport["eyr"], 2020, 2030) {
		return true, false
	}

	tmp := []rune(passport["hgt"])
	hgtLen := len(tmp)
	hgt, _ := strconv.Atoi(string(tmp[0 : hgtLen-2]))
	unit := string(tmp[hgtLen-2:])
	if unit != "cm" && unit != "in" {
		return true, false
	}
	if unit == "cm" && (hgt < 150 || hgt > 193) {
		return true, false
	}
	if unit == "in" && (hgt < 59 || hgt > 76) {
		return true, false
	}

	if !regexp.MustCompile(`^#[\dabdcdef]{6}$`).MatchString(passport["hcl"]) {
		return true, false
	}
	if !regexp.MustCompile(`^\d{9}$`).MatchString(passport["pid"]) {
		return true, false
	}

	ecl, _ := eyeColors.Contains(passport["ecl"])
	if !ecl {
		return true, false
	}

	return true, true
}

func main() {
	data, _ := ioutil.ReadFile("./solutions/4/data.txt")
	passportsRaw := strings.Split(strings.TrimSpace(string(data)), "\n\n")
	passports := []tPassport{}

	re := regexp.MustCompile(`\n|\s`)
	for _, passportRaw := range passportsRaw {
		passport := tPassport{}
		entries := re.Split(passportRaw, -1)
		for _, entry := range entries {
			split := strings.Split(entry, ":")
			passport[split[0]] = split[1]
		}
		passports = append(passports, passport)
	}

	validSimple := 0
	validComplex := 0
	for _, passport := range passports {
		simple, complex := verifyPassport(passport)
		if simple {
			validSimple++
		}
		if complex {
			validComplex++
		}
	}
	fmt.Println("Simple Validation:\t", validSimple)
	fmt.Println("Extended Validation:\t", validComplex)
}
