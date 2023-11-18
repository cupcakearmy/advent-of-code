---
inject: true
to: cargo.toml
before: "# INJECT HERE"
skip_if: <%= id %> 
---

[[bin]]
name = "<%= id %>"
path = "<%= dir %>/rust/main.rs"
