# CPU cache associativity

The memory cache can work under three different configurations: direct mapping, fully associative and set associative (a.k.a. n-way set associative).

![](images/-5d44c91c-69b2-4fc1-b174-6cc766f3311euntitled)

# Direct mapping

Each entry in main memory can go in just one place in the cache.

# Fully-associative

The replacement policy is free to choose any entry in the cache to hold the copy.

# N-way set associative

Each entry in main memory can go to any one of N places in the cache

# Trade-off

## Higher associativity

- Needs to check more places, which takes more power and chip area, and potentially more time.
- Less cache misses

## Lower associativity

- Faster search
- More cache misses

![](images/-9d2fcd91-46c1-47d7-9479-dcdae1282e81untitled)

# Reference

[CPU cache - Wikipedia](https://en.wikipedia.org/wiki/CPU_cache)

[How L1 and L2 CPU Caches Work, and Why They're an Essential Part of Modern Chips - ExtremeTech](https://www.extremetech.com/extreme/188776-how-l1-and-l2-cpu-caches-work-and-why-theyre-an-essential-part-of-modern-chips)