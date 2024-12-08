#![feature(test)]

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

struct Point {
    x: usize,
    y: usize,
}

fn part_a(input: &str) {
    let result = input.trim();

    let lines = result.split("\n").collect::<Vec<&str>>();

    let mut symbols: Vec<Vec<usize>> = Vec::new();
    for _ in [0..lines.len()] {
        symbols.push(vec![0; 0]);
    }

    for (y, line) in result.split("\n").enumerate() {
        for (x, char) in line.chars().enumerate() {
            match char {
                '*' | '&' | '+' | '#' | '$' => symbols[y].push(x),
                _ => {}
            }
        }
    }

    println!("{:?}", symbols);
}

fn part_b(input: &str) {
    let result = input.trim();
    println!("{}", result);
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    // part_a(INPUT);

    println!("\nPart B:");
    // part_b(TEST);
    // part_b(INPUT);
}
