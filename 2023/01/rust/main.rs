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
    let result = input
        .trim()
        .split("\n")
        .map(|line| {
            let mut first: u16 = 0;
            for char in line.chars() {
                if first != 0 {
                    break;
                }
                match char {
                    '1' => first = 1,
                    '2' => first = 2,
                    '3' => first = 3,
                    '4' => first = 4,
                    '5' => first = 5,
                    '6' => first = 6,
                    '7' => first = 7,
                    '8' => first = 8,
                    '9' => first = 9,
                    _ => continue,
                }
            }
            let mut last: u16 = 0;
            for char in line.chars().rev() {
                if last != 0 {
                    break;
                }
                match char {
                    '1' => last = 1,
                    '2' => last = 2,
                    '3' => last = 3,
                    '4' => last = 4,
                    '5' => last = 5,
                    '6' => last = 6,
                    '7' => last = 7,
                    '8' => last = 8,
                    '9' => last = 9,
                    _ => continue,
                }
            }
            return first * 10 + last;
        })
        .sum::<u16>();
    println!("{}", result);
}

fn part_b(input: &str) {
    let result = input
        .trim()
        .split("\n")
        .map(|line| {
            let mut first: usize = 0;
            let nums = [
                "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine",
            ];
            for (i, s) in nums.iter().enumerate() {
                if line.starts_with(s) {
                    first = if i < 9 { i + 1 } else { i - 8 };
                    break;
                }
                line.split_at(mid)
            }
            let mut last = 0 as usize;
            return first * 10 + last;
        })
        .sum::<usize>();
    println!("{}", result);
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    part_a(INPUT);

    println!("\nPart B:");
    part_b(TEST);
    // part_b(INPUT);
}
