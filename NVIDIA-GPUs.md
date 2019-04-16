# NVIDIA GPUs

# Taxonomy

## Compute capability (version)

Hardware design, number of cores, cache size, and supported arithmetic instructions are different for different versions of **compute capability**. NVIDIA Tesla K20s on Stampede are based on the Kepler GPU architecture with compute capability 3.5.

When programming with CUDA, it is very important to be aware of the differences among different versions of hardware. In CUDA, **hardware version is referred to as compute capability.** For example, compute capability 1.x devices have 16KB local memory per thread, and 2.x and 3.x devices have 512KB local memory per thread.

If you want to program your NVIDA graphics card on your personal computer, be sure to know your device's [compute capability](http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#compute-capabilities).

## GeForce, Quadro, Tesla

2006년 11월 GeForce 8800 GTX 이후 생산되는 GPU

- GeForce: 일반적인 Graphic Card
- Quadro: 고성능의 Graphic 작업 전용
- Tesla: Graphic 기능 없이 고성능 연산 전용. GPGPU cards. Nvidia Tesla is Nvidia's brand name for their products targeting stream processing or general-purpose graphics processing units (GPGPU).

# Nvidia Graphics processing units

[Nvidia GPUs](https://www.notion.so/ec4f66cb7e8d4843b20f445e198ab163)

## Highlights

- M40
    - Tesla (only for computing)
    - Maxwell
- 1080 Ti, 1080
    - GeForce GTX
    - Pascal
- Titan X
    - GeForce
    - Pascal
- Tesla P40
    - Tesla
    - Pascal
- Titan V
    - GeForce
    - Volta
- V100
    - Tesla
    - Volta
- Titan RTX, 2080Ti, 2080
    - GeForce
    - Turing

# Reference

[CUDA - Wikipedia](https://en.wikipedia.org/wiki/CUDA)

[List of Nvidia graphics processing units - Wikipedia](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units#GeForce_900_series)

[](https://cvw.cac.cornell.edu/gpu/computecap)