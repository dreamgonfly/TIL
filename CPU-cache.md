# CPU cache

A CPU cache is a hardware cache used by CPU to reduce the cost to access data from the main memory.

![](images/-44995e9d-ce97-47bb-81e0-6f273133deb8untitled)

# Levels

## L1

L1 is "level-1" cache memory, usually built onto the microprocessor chip itself. Almost all current CPUs' L1 cache is split into L1d (for data) and L1i (for instructions). For example, the Intel MMX microprocessor comes with 32 thousand bytes of L1.

## L2

L2 (that is, level-2) cache memory is on a separate chip (possibly on an expansion card) that can be accessed more quickly than the larger "main" memory. The L2 cache is usually not split and acts as a common repository for the already split L1 cache. L2 cache is usually not shared between the cores. A popular L2 cache memory size is 1,024 kilobytes (one megabyte).

## L3 and higher

The L3 cache, and higher-level caches, are shared between the cores and are not split.

## Last Level Cache (LLC)

Last level cache (LLC) refers to the highest-level cache, which is shared by all the functional units on the chip and is called before accessing memory.

![](images/-446591ac-9f67-4557-aa1a-c08d6e3febc2untitled)

# Cache entry

Data is transferred between memory and cache in blocks of fixed size, called **cache line**s or **cache block**s. When a cache line is copied from memory into the cache, a **cache entry** is created. The cache entry will include the copied data as well as the requested memory location (called a **tag**).

![](images/-9cb56b37-2156-499f-8815-fede2f98125buntitled)

# Cache hit & miss

When the processor needs to read or write a location in memory, it first checks for a corresponding entry in the cache. The cache checks for the contents of the requested memory location in any cache lines that might contain that address. If the processor finds that the memory location is in the cache, a **cache hit** has occurred. However, if the processor does not find the memory location in the cache, a **cache miss** has occurred. In the case of a cache hit, the processor immediately reads or writes the data in the cache line. For a cache miss, the cache allocates a new entry and copies data from main memory, then the request is fulfilled from the contents of the cache.

# CPU stalls

The time taken to fetch one cache line from memory (read latency due to a cache miss) matters because the CPU will run out of things to do while waiting for the cache line. When a CPU reaches this state, it is called a **stall**. 

# Why it matters: the speed gap

The speed gap between the memory performance and the processor performance is increasing exponentially. Modern CPUs can execute hundreds of instructions in the time taken to fetch a single cache line from main memory. 

As CPUs become faster compared to main memory, stalls due to cache misses displace more potential computation.

# Out-of-order execution & hyper-threading

Various techniques have been employed to keep the CPU busy during CPU stalls, including out-of-order execution in which the CPU (Pentium Pro and later Intel designs, for example) attempts to execute independent instructions after the instruction that is waiting for the cache miss data. 

Another technology, used by many processors, is simultaneous multithreading (SMT), or‍—‌in Intel's terminology‍—‌hyper-threading (HT), which allows an alternate thread to use the CPU core while the first thread waits for required CPU resources to become available.

# Example

## Intel Core i9-9900K

Core i9-9900K is a 64-bit octa-core high-end performance x86 desktop microprocessor introduced by Intel in late 2018. This processor, which is based on the Coffee Lake microarchitecture, is manufactured on Intel's 3rd generation enhanced 14nm++ process. The i9-9900K operates at a 3.6 GHz with a TDP of 95 W and a Turbo Boost frequency of up to 5 GHz.

![](images/-f2a10cf0-3096-4136-8532-50164d934273untitled)

# Reference

[CPU cache - Wikipedia](https://en.wikipedia.org/wiki/CPU_cache)

[GT Explains: What is a CPU Cache, What Does it Do](https://www.guidingtech.com/53366/cpu-cache-explained/)

[What is L1 and L2? - Definition from WhatIs.com](https://whatis.techtarget.com/definition/L1-and-L2)

[Last Level Cache (LLC) - WikiChip](https://en.wikichip.org/wiki/last_level_cache)

[Core i9-9900K - Intel - WikiChip](https://en.wikichip.org/wiki/intel/core_i9/i9-9900k)