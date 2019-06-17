# Register

A **processor register** (**CPU register**) is one of a small set of data holding places that are part of the computer processor.

![](Untitled-51d171eb-c181-4d9c-9d21-76ff72239be2.png)

A register may hold an [instruction](https://whatis.techtarget.com/definition/instruction), a storage address, or any kind of data (such as a bit sequence or individual characters). Some instructions specify registers as part of the instruction. For example, an instruction may specify that the contents of two defined registers be added together and then placed in a specified register.

A register must be large enough to hold an instruction - for example, in a [64-bit computer](https://searchdatacenter.techtarget.com/definition/64-bit-processor), a register must be 64 [bits](https://whatis.techtarget.com/definition/bit-binary-digit) in length. In some computer designs, there are smaller registers - for example, *half-registers* - for shorter instructions. Depending on the processor design and language rules, registers may be numbered or have arbitrary names.

# Types of registers

## MAR

The **MAR (Memory Address Register)** holds the memory addresses of data and instructions. This register is used to access data and instructions from memory during the execution phase of an instruction. Suppose CPU wants to store some data in the memory or to read the data from the memory. It places the address of the-required memory location in the MAR.

## PC

The **program counter (PC)**, commonly called the **instruction pointer** (IP) in Intel x86 microprocessors, and sometimes called the **instruction address register**, or just part of the instruction sequencer in some computers, is a processor register.

It is a 16 bit special function register in the 8085 microprocessor. It keeps track of the the next memory address of the instruction that is to be executed once the execution of the current instruction is completed. In other words, it holds the address of the memory location of the next instruction when the current instruction is executed by the microprocessor.

## ACC

This Register is used for storing the Results those are produced by the system. When the CPU will generate some results after the processing then all the results will be stored into the **ACC Register**.

## MDR

**MDR (Memory Data Register)** is the register of a [computer](http://ecomputernotes.com/fundamental/introduction-to-computer/what-is-computer)'s [control unit](http://ecomputernotes.com/fundamental/introduction-to-computer/control-unit) that contains the **data to be stored in the computer storage** (e.g. RAM), or the **data after a fetch from the computer storage**. It acts **like a buffer** and holds anything that is copied from the memory ready for the processor to use it. **MDR hold the [information](http://ecomputernotes.com/fundamental/information-technology/what-do-you-mean-by-data-and-information) before it goes to the decoder.**

MDR which contains the data to be written into or readout of the addressed location. For example, to retrieve the contents of cell 123, we would load the value 123 (in binary, of course) into the MAR and perform a fetch operation. When the operation is done, a copy of the contents of cell 123 would be in the MDR. To store the value 98 into cell 4, we load a 4 into the MAR and a 98 into the MDR and perform a store. When the operation is completed the contents of cell 4 will have been set to 98, by discarding whatever was there previously.

### Index Register  ****

A hardware element which holds a number that can be added to (or, in some cases, subtracted from) the address portion of a computer instruction to form an effective address. Also known as **base register**. An index register in a computer's CPU is a processor register used for modifying operand addresses during the run of a program.

### Memory Buffer Register

MBR stand for ***Memory Buffer Register***. This register holds the contents of data or instruction read from, or written in memory. It means that this register is used to store data/instruction coming from the memory or going to the memory.

### Data Register

A register used in microcomputers to temporarily store data being transmitted to or from a peripheral device.

# Reference

[What is register (processor register, CPU register)? - Definition from WhatIs.com](https://whatis.techtarget.com/definition/register)

[Register - What is Registers? Types of Registers](http://ecomputernotes.com/fundamental/input-output-and-memory/what-is-registers-function-performed-by-registers-types-of-registers)