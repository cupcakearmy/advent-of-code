---
to: <%= dir %>/rust/main.rs
unless_exists: true
---
fn main() {
    // Part A
    let contents = include_str!("../test.txt").trim();
    println!("A: {}", contents);
}
