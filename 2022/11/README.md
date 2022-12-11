# 11

## Part one

Easy, fun, lets go.

## Part two

Performance was the issue. I started moving functions to inline code (reduce readability for less function calls). It did not make a dent.

Lesson learned: In python functions calls and destructuring are not expensive.

What helped a bit was:

- Precalculating if it's a multiplication or addition for each monkey.
- And whether to use the old value or a custom one.

However that was not nearly enough of a speed boost to get me to the performance needed.

**Enter math**: We are always diving, so what if I could make the numbers smaller somehow? But everyone uses a different divider? Thats when it struck me! Before passing the item to the next monkey, reduce it with modulo by the biggest common denominator of all monkeys (since the divisions will not influence the other decisions of the other monkeys). And it worked! Speed was no issue anymore ⚡️

<details>
  <summary>Solutions</summary>
  <ol>
    <li>58322</li>
    <li>13937702909</li>
  </ol>
</details>
