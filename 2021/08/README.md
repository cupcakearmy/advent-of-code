# 08

This was super fun and another episode of "I should have gotten my paper out sooner".

As soon as I realized you can take the statistical approach to decode the numbers.

1. Count all characters

This will reveal the mapping for the letters `b`, `e` and `f`, as they appear a unique amount of times.

2. `a` & `c`

Both appear 8 times. We find `a` by looking at the `1` and `7`. If we identify `1` (cf) and `7` (afc) we can simply calculate what `a` is by difference. With `a` identified `c` is also determined.

3. `d` & `g`

Both appear 7 times. We take the similar approach as in 2.

This ensures a linear time execution.

<details>
  <summary>Solutions</summary>
  <ol>
    <li>449</li>
    <li>968175</li>
  </ol>
</details>
