---
to: <%= dir %>/rust/main.rs
unless_exists: true
---
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

fn part_a(input: &str) {
    let result = input.trim();
    println!("{}", result);
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
    part_b(TEST);
    // part_b(INPUT);
}
