# Memory bandwidth

Memory bandwidth is basically the speed of the RAM. It's the rate at which data can be read from or stored into a memory by a processor. It's measured in gigabytes per second (GB/s).

# **Computation**

The total bandwidth is the product of:

- Memory clock: Base RAM clock frequency
- Memory type: Number of data transfers per clock
- Memory width: Memory bus (interface) width

## Memory clock

The memory clock is the clock rate of the memory chips. RAM is running at a clock speed. RAM running at 1 GHz "ticks" 1,000,000,000 (a billion) times a second. With every tick, it can receive or send one bit on every lane. So a theoretical RAM module with only one memory lane running at 1GHz would deliver 1 Gigabit per second, since there are 8 bits to the bytes that means 125 Megabyte per second.

## Memory type

The most common memory type is double data rate (DDR) which means that it transfers two memory values for each memory clock cycle. There are also other kinds of DDR like DDR2, GDDR3, and GDDR4 and they also transfer at twice the memory clock rate. Some very old video cards still use single data rate (SDR) which transfers one value per clock cycle.

GDDR5 is "quad-pumped" and delivers four bits per tick. Really GDDR5 should have been called QDR not DDR, as it was no longer Double Data Rate, it was Quad Data Rate. GDDR5X and GDDR6 are both Octo Data Rate.

**Effective clock speed**: Memory clock X GDDR type multiplier

## Memory width

RAM doesn't just have one single lane to send data. Even the Intel 4004 had a 4 bit bus. Each DDR, DDR2, or DDR3 memory interface is 64 bits wide. The memory width of the common cards range from 32 bits to 256 bits.

# Example

## NVIDIA GeForce RTX 2080Ti

Effective memory clock: Memory clock (1750 MHz) X GDDR type multiplier (8)

Memory Bandwidth (616.0 GB/s) = Effective memory clock X Memory width (352 bit) / 8 (change from bit to byte)

![](images/-9ad00912-912c-4727-80a1-329c8dc5af16untitled)

![](images/-f5ceb3dc-ea40-44ce-b5ca-0f024706178euntitled)

[NVIDIA GeForce RTX 2080 Ti Specs](https://www.techpowerup.com/gpu-specs/geforce-rtx-2080-ti.c3305)

# Reference

[Understanding video RAM memory bandwidth](http://www.playtool.com/pages/vramwidth/width.html)

[Memory bandwidth - Wikipedia](https://en.wikipedia.org/wiki/Memory_bandwidth)

[](https://stackoverflow.com/questions/15055877/how-to-get-memory-bandwidth-from-memory-clock-memory-speed)

[How to calculate GDDR6 speed from GPU-Z?](https://www.techpowerup.com/forums/threads/how-to-calculate-gddr6-speed-from-gpu-z.250747/)

[Explain to me how memory width (128/192/256 bit, etc) is related to memory amount.](https://www.techpowerup.com/forums/threads/explain-to-me-how-memory-width-128-192-256-bit-etc-is-related-to-memory-amount.170588/)