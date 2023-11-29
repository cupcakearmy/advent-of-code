# Advent Of Code

Template repository for Advent of Code. It automatically downloads your puzzle inputs and bootstraps files for the following languages:

- Typescript
- Python
- Rust

Have fun! 🤗🎄

## Getting started

New "days" are generated with [`hygen`](https://github.com/jondot/hygen). This will bootstrap code for python and rust. See details about the specifica languages below

```bash
# First time setup
bun i

# Put the Advent of Code token into .env

# Generate day
bun run gen --year 2022 --day 1
```

## Languages

Below are instructions for the specific handling of each language included.

### Typescript

Run a single day:

```bash
# Once
bun run 2022/01/typescript/main.ts

# Rerun on change
bun run --watch 2022/01/typescript/main.ts
```

### Python

```bash
# Get a python enabled shell, with the latest version
poetry shell

# Run once
python 2022/01/python/main.py

# Rerun on change
bunx nodemon 2022/01/python/main.py
```

### Rust

Run a single day:

```bash
# Once
cargo run --bin 2022-01

# Rerun on change (requires: https://github.com/watchexec/cargo-watch)
cargo watch -x 'run --bin 2022-01'
```

Benchmark a day:

```bash
cargo bench --bin 2022-01
```

Benchmark all days:

```bash
cargo bench
```

> The benchmark is the built in Rust one. This is the [reason](https://doc.rust-lang.org/cargo/commands/cargo-bench.html) for the _nightly_ version.
