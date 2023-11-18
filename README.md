# Advent Of Code

## Getting started

New "days" are generated with [`hygen`](https://github.com/jondot/hygen). This will bootstrap code for python and rust. See details about the specifica languages below

```bash
# First time setup
bun i

# Generate
bun run gen --year 2022 --day 1
```

## Python

## Rust

Run a single day:

```bash
cargo run --bin 2022-01
```

Bench a day:

```bash
cargo bench --bin 2022-01
```

Bench all days:

```bash
cargo bench
```

> The benchmark is the built in Rust one. This is the [reason](https://doc.rust-lang.org/cargo/commands/cargo-bench.html) for the _nightly_ version.
