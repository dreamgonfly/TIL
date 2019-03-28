# Register

A register or a **processor register** is a quickly accessible location available to a computer's central processing unit (CPU). Registers usually consist of a small amount of fast storage and are at the top of the memory hierarchy, providing the fastest way to access data.

![](Untitled-78a555b8-61a3-447a-92ab-cb95346cf84f.png)

# Types

- **User-accessible registers** can be read or written by machine instructions. The most common division of user-accessible registers is into data registers and address registers.
    - **Data registers**
    - **Address registers** hold addresses and are used by instructions that indirectly access memory.
        - The **stack pointer** is used to manage the run-time stack.
    - **General-purpose registers** can store both data and addresses.
    - **Floating-point registers** store floating point numbers.
    - **Vector registers** hold data for vector processing done by SIMD instructions (Single Instruction, Multiple Data).
    - **Special-purpose registers**
- **Internal registers** – registers not accessible by instructions, used internally for processor operations.
    - **Instruction register**, holding the instruction currently being executed.
    - Registers related to fetching information from RAM, a collection of storage registers located on separate chips from the CPU:
        - [**Memory buffer register**](https://en.wikipedia.org/wiki/Memory_buffer_register) (MBR)
        - [**Memory data register**](https://en.wikipedia.org/wiki/Memory_data_register) (MDR)
        - [**Memory address register**](https://en.wikipedia.org/wiki/Memory_address_register) (MAR)
- **Architectural register** - The registers visible to software defined by an architecture may not correspond to the physical hardware, if there is [register renaming](https://en.wikipedia.org/wiki/Register_renaming) being performed by underlying hardware.

![](Untitled-7ed69212-4af0-4675-8b75-53a9094ead18.png)

# Architectural register

An architectural register is a register implied by the instruction set architecture of the processor you're using. It's architectural, in the sense that the architecture definition says that the register must exist, or at the very least, an implementation must give the *illusion* that the register exists. Architectural registers are the registers the programmer needs to be aware of when programming in assembly language. When an assembly programmer thinks of a specific register by name, most often they're thinking of an architectural register.

# Register size

For many years, registers were 32-bit, but now many are 64-bit in size. A 64-bit register is necessary for a 64-bit processor, since it enables the CPU to access 64-bit memory addresses. A 64-bit register can also store 64-bit instructions, which cannot be loaded into a 32-bit register. Therefore, most programs written for 32-bit processors can run on 64-bit computers, while 64-bit programs are not backwards compatible with 32-bit machines.

# Number of registers

Some processors have 8 registers while others have 16, 32, or more. 

# Register file

A register file is an array of processor registers in a central processing unit (CPU).

The instruction set architecture of a CPU will almost always define a set of registers which are used to stage data between memory and the functional units on the chip. In simpler CPUs, these architectural registers correspond one-for-one to the entries in a physical register file (PRF) within the CPU. More complicated CPUs use **register renaming**, so that the mapping of which physical entry stores a particular architectural register changes dynamically during execution

# Vector processor

a vector processor or array processor is a central processing unit (CPU) that implements an instruction set containing instructions that operate on one-dimensional arrays of data called vectors, compared to scalar processors, whose instructions operate on single data items.

As of 2015 most commodity CPUs implement architectures that feature instructions for a form of vector processing on multiple (vectorized) data sets. Common examples include Intel x86's MMX, SSE and AVX instructions, AMD's 3DNow! extensions, Sparc's VIS extension, PowerPC's AltiVec and MIPS' MSA.

# Reference

[Processor register - Wikipedia](https://en.wikipedia.org/wiki/Processor_register)

[How many registers are there in the CPU?](https://www.quora.com/How-many-registers-are-there-in-the-CPU)

[Register Definition](https://techterms.com/definition/register)

[Register file - Wikipedia](https://en.wikipedia.org/wiki/Register_file)

[Vector processor - Wikipedia](https://en.wikipedia.org/wiki/Vector_processor)