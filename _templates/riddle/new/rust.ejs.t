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
        b.iter(|| part_a());
    }

    #[bench]
    fn bench_b(b: &mut Bencher) {
        b.iter(|| part_b());
    }
}

fn part_a() {
    let result = include_str!("../input.txt");
    println!("A: {}", result);
}

fn part_b() {
    let result = include_str!("../input.txt");
    println!("A: {}", result);
}

fn main() {
    part_a();
    part_b();
}
