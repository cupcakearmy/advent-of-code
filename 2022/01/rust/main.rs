fn main() {
    // Part A
    let result: u32 = include_str!("../input.txt")
        .trim()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum())
        .max()
        .unwrap();
    println!("A: {}", result);
}
