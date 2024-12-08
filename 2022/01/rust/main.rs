#![feature(test)]

extern crate test;

#[cfg(test)]
mod tests {
    use super::*;
    use test::{black_box, Bencher};

    #[bench]
    fn bench_a(b: &mut Bencher) {
        b.iter(|| black_box(part_a(INPUT)));
    }

    #[bench]
    fn bench_b(b: &mut Bencher) {
        b.iter(|| black_box(part_b(INPUT)));
    }
}

const INPUT: &str = include_str!("../input.txt");
const TEST: &str = include_str!("../test.txt");

fn part_a(input: &str) {
    let result: u32 = input
        .trim()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum())
        .max()
        .unwrap();
    println!("{}", result);
}

fn part_b(input: &str) {
    let mut result = input
        .trim()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum::<u32>())
        .collect::<Vec<u32>>();
    result.sort_unstable();
    let total = result.into_iter().rev().take(3).sum::<u32>();
    println!("{}", total);
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    part_a(INPUT);

    println!("\nPart B:");
    part_b(TEST);
    part_b(INPUT);
}
