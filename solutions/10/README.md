# 10

# First

The first one is really easy. Just sort, make the diff and count.
First I take the list and sort it:

```python
[16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
[0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22] # Sorted and added the wall plug (0) and the phone (biggest + 3)
[1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3] # The size of each step
```

Now we can simply count how many `1` and `3` there are with `l.count(1)`.

## Second

This is where it gets tricky.

First lets find all the consecutive `1`s ad only they can be removed. If we have more than 1 consecutive `1` we can remove one of it. However we need to be careful not to remove to many or the step will be higher than `3` and the chain breaks.

```python
[1, 1, 1, 1] # We can transform this example by adding 2 numbers together and "joining" them.

[1, 2, 1] # Valid
[1, 1, 2] # Valid
[1, 3] # Valid
[4] # Invalid because we can jump a max of 3 steps at a time.
```

Now we could iterate but I wanted to find a formula. Not sure this is correct but here we go.

Basically we take the length of the consecutive `1` and compute `2**(l-1)` to get all possible combinations.
Now we need to subtract the possible `4` which can only be achieved if we have at least 4 numbers -> `floor(l/4)`
For a grand total of `2**(l-1) - floor(l/4)`

<details>
  <summary>Solutions</summary>
  <ol>
    <li>2475</li>
    <li>442136281481216</li>
  </ol>
</details>
