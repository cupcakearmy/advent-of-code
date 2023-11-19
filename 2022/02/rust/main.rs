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
    fn bench_a_old(b: &mut Bencher) {
        b.iter(|| part_a_old(INPUT));
    }

    #[bench]
    fn bench_b(b: &mut Bencher) {
        b.iter(|| part_b(INPUT));
    }
}

const TEST: &str = include_str!("../test.txt");
const INPUT: &str = include_str!("../input.txt");

#[derive(Debug, Clone, Copy)]
enum Type {
    Rock = 1,
    Paper = 2,
    Scissor = 3,
}

#[derive(Debug)]
struct Game(Type, Type);

impl Game {
    fn score(&self) -> u32 {
        let mut total = self.0 as u32;
        // Result will be: 0=draw 1=win 2=loss
        let result = (self.0 as i8 - self.1 as i8).rem_euclid(3) as u8;
        total += match result {
            1 => 6,
            0 => 3,
            _ => 0,
        };
        total
    }
}

fn part_a_old(input: &str) {
    let result = input
        .trim()
        .lines()
        .map(|line| {
            let opponent: Type = match line.chars().nth(0).unwrap() {
                'A' => Type::Rock,
                'B' => Type::Paper,
                'C' => Type::Scissor,
                _ => panic!("unkown input"),
            };
            let me = match line.chars().nth(2).unwrap() {
                'X' => Type::Rock,
                'Y' => Type::Paper,
                'Z' => Type::Scissor,
                _ => panic!("unkown input"),
            };
            let g: Game = Game(me, opponent);
            g.score()
        })
        .sum::<u32>();
    println!("A: {:?}", result);
}

fn part_a(input: &str) {
    let result = input
        .trim()
        .lines()
        .map(|line| {
            let bytes = line.as_bytes();
            let opponent = bytes[0] - b'A';
            let me: u8 = bytes[2] - b'X';

            let total = me + 1;
            // Result will be: 0=draw 1=win 2=loss
            let result = (me as i8 - opponent as i8).rem_euclid(3);
            let score = match result {
                1 => 6,
                0 => 3,
                _ => 0,
            };
            (total + score) as u16
        })
        .sum::<u16>();
    println!("{}", result);
}

fn part_b(input: &str) {
    let result = input
        .trim()
        .lines()
        .map(|line| {
            let bytes = line.as_bytes();
            let opponent = bytes[0] - 'A' as u8;
            let result: u8 = bytes[2] - 'X' as u8;

            let total: u8 = match result {
                1 => 3,
                2 => 6,
                _ => 0,
            };
            let me = (opponent + result + 2).rem_euclid(3);
            (total + me + 1) as u16
        })
        .sum::<u16>();
    println!("{}", result);
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    part_a(INPUT);

    println!("\nPart B:");
    part_b(TEST);
    part_b(INPUT);
}
