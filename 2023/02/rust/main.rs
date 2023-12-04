#![feature(test)]

use std::cmp;

extern crate test;

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[bench]
    fn bench_a(b: &mut Bencher) {
        b.iter(|| part_a(INPUT));
    }

    #[bench]
    fn bench_b(b: &mut Bencher) {
        b.iter(|| part_b(INPUT));
    }
}

const INPUT: &str = include_str!("../input.txt");
const TEST: &str = include_str!("../test.txt");

#[derive(Debug)]
struct Round {
    red: usize,
    blue: usize,
    green: usize,
}

fn max_for_game(s: &str, calc: impl Fn(Round) -> usize) -> usize {
    let max = s
        .split(";")
        .map(|round| {
            // Max count
            let mut r = Round {
                blue: 0,
                green: 0,
                red: 0,
            };
            for pick in round.split(",") {
                let parts: Vec<&str> = pick.trim().split(" ").collect();
                let num: usize = parts[0].parse().unwrap();
                match parts[1] {
                    "blue" => r.blue = num,
                    "green" => r.green = num,
                    "red" => r.red = num,
                    _ => panic!("Invalid color {}", parts[1]),
                }
            }
            r
        })
        .reduce(|a, b| Round {
            red: cmp::max(a.red, b.red),
            blue: (cmp::max(a.blue, b.blue)),
            green: (cmp::max(a.green, b.green)),
        })
        .unwrap();
    calc(max)
}

fn parse_game_b(s: &str) -> usize {
    let splitted: Vec<&str> = s.split(":").collect();
    max_for_game(splitted[1], |x| x.blue * x.green * x.red)
}

fn part_a(input: &str) {
    let result: usize = input
        .trim()
        .split("\n")
        .map(|line| {
            let splitted: Vec<&str> = line.split(":").collect();
            max_for_game(splitted[1], |r| {
                if r.red <= 12 && r.green <= 13 && r.blue <= 14 {
                    splitted[0].split_at(5).1.parse().unwrap()
                } else {
                    0
                }
            })
        })
        .sum();
    println!("{result}");
}

fn part_b(input: &str) {
    let result: usize = input
        .trim()
        .split("\n")
        .map(|line| {
            return parse_game_b(line);
        })
        .sum();
    println!("{result}");
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    part_a(INPUT);

    println!("\nPart B:");
    part_b(TEST);
    part_b(INPUT);
}
