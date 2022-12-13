# 12

What a ride...

So first I tried without A-Star. Well that of course did not stand a chance against the actual dataset.

I think my a start implementation is flawed, of the heuristics are not optimal. It starts in a straight line, but ends up checking every field anyways. So it's more like a Dijkstra. But it works.
The difference between Manhattan and Euclidean distance as `h(x)` did not help two. Went form 6939 iterations to 6974.

The second part was quick. I reversed the search, starting from the end, removed the heuristic, so ti's now a classic Dijkstra, and instead of searching for a specific node, i stopped at the first encounter of an `a` or `0` elevation.

<details>
  <summary>Solutions</summary>
  <ol>
    <li>497</li>
    <li>492</li>
  </ol>
</details>
