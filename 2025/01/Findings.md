# Day 01

> First of all, what a joy not having 24 days, and no leaderboard. I actually really enjoy it and get more out of it. Turn off LLM, and just have fun 🤩

## Part 1

That was quite straight forward, nothing notable here. But it has been a while since I last used mod.

## Part 2

This was fun. So i wanted to (of course) not brute force it. Solution: first: calculate how many "empty" rounds the instruction had. e.g. `L106` would become simply `L6`) and simply increase by one. Now counting if we crossed `0` was interesting. I calculated the _distance to zero_ by checking how far the zero was, depending on the direction. And then simply seeing if the distance to travel was equally greater than the distance to zero.

The gotcha which took me a few minutes, was that I was adding a zero to much, if I was starting at `0`. But the test data caught that as well!
