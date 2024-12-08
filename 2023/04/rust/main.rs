#![feature(test)]

use std::collections::HashMap;

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

fn get_matches_per_card(input: &str) -> Vec<usize> {
    input
        .trim()
        .split("\n")
        .map(|line| {
            let splitted: Vec<&str> = line.split(":").collect();
            let body = splitted[1]
                .split("|")
                .map(|part| {
                    let mut numbers = part
                        .trim()
                        .split(" ")
                        .filter(|x| x.len() > 0)
                        .map(|s| s.parse::<usize>().expect("not a number"))
                        .collect::<Vec<usize>>();
                    numbers.sort();
                    numbers
                })
                .collect::<Vec<Vec<usize>>>();

            let numbers = &body[0];
            let winning = &body[1];

            let mut matches = 0_usize;
            for number in numbers {
                match winning.binary_search(number) {
                    Err(_) => {}
                    Ok(_) => matches += 1,
                }
            }

            matches
        })
        .collect()
}

fn part_a(input: &str) {
    let matches = get_matches_per_card(input);
    let total: usize = matches
        .iter()
        .map(|matches| {
            if *matches > 0 {
                2_usize.pow(*matches as u32 - 1)
            } else {
                0
            }
        })
        .sum();

    println!("{total}");
}

fn add_points(matches: &Vec<usize>, cache: &mut HashMap<usize, usize>, number: usize) -> usize {
    let cached = cache.get(&number);
    match cached {
        Some(x) => *x,
        None => {
            let m = matches[number];
            if m == 0 {
                return 0;
            }
            let mut total = 0;
            for n in number + 1..(number + m) {
                total += add_points(matches, cache, n);
            }
            cache.insert(number, total);
            total
        }
    }
}

fn part_b(input: &str) {
    let matches = get_matches_per_card(input);
    let mut cache: HashMap<usize, usize> = HashMap::new();
    let mut scores = vec![0, matches.len()];
    let mut total: usize = 0;
    for m in matches {
        // total += add_points(&matches, &mut cache, m);
    }
    // let total: usize = matches
    //     .iter()
    //     .map(|matches| {
    //         if *matches > 0 {
    //             2_usize.pow(matches - 1)
    //         } else {
    //             0
    //         }
    //     })
    //     .sum();

    // println!("{total}");
}

fn main() {
    println!("Part A:");
    part_a(TEST);
    part_a(INPUT);

    println!("\nPart B:");
    part_b(TEST);
    // part_b(INPUT);
}
