# 3

We can simply parse the forest as an array of strings.
The trees repeat infinitely to the right, this screams for a good mod.
This means: `char = row[x % len(row)]`. No complex logic needed

For the second one we simply automate the process and sum up the total.
We can simply encode the coordinates as a function of the index we are current at.

<details>
  <summary>Solutions</summary>
  <ol>
    <li>252</li>
    <li>57 * 252 * 64 * 66 * 43 = 2608962048</li>
  </ol>
</details>
