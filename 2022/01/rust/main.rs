#![feature(test)]

extern crate test;

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[bench]
    fn bench_a(b: &mut Bencher) {
        b.iter(|| part_a());
    }

    #[bench]
    fn bench_b(b: &mut Bencher) {
        b.iter(|| part_b());
    }
}

fn part_a() {
    let result: u32 = include_str!("../input.txt")
        .trim()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum())
        .max()
        .unwrap();
    println!("A: {}", result);
}

fn part_b() {
    let mut result = include_str!("../input.txt")
        .trim()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum::<u32>())
        .collect::<Vec<u32>>();
    result.sort_unstable();
    let total = result.into_iter().rev().take(3).sum::<u32>();
    println!("B: {}", total);
}

fn main() {
    part_a();
    part_b();
}
