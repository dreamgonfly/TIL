# The stack and the heap

# Memory segments

The memory that a program uses is typically divided into a few different areas, called **segments**:

- The code segment (also called a text segment), where the compiled program sits in memory. The code segment is typically read-only.
- The bss segment (also called the uninitialized data segment), where zero-initialized global and static variables are stored.
- The data segment (also called the initialized data segment), where initialized global and static variables are stored.
- The heap, where dynamically allocated variables are allocated from.
- The call stack, where function parameters, local variables, and other function-related information are stored.

# Stack

The stack or the **call stack** keeps track of all the active functions (those that have been called but have not yet terminated) from the start of the program to the current point of execution, and handles allocation of all function parameters and local variables.

Stack memory is used for **execution of a thread**. They contain method specific values that are short-lived and references to other objects in the heap that are getting referred from the method.

- very fast access
- don't have to explicitly de-allocate variables
- space is managed efficiently by CPU, memory will not become fragmented
- local variables only
- limit on stack size (OS-dependent)
- variables cannot be resized

## Mailbox analogy

Consider a bunch of mailboxes, all stacked on top of each other. Each mailbox can only hold one item, and all mailboxes start out empty. Furthermore, each mailbox is nailed to the mailbox below it, so the number of mailboxes can not be changed. If we can’t change the number of mailboxes, how do we get a stack-like behavior?

First, we use a marker (like a post-it note) to keep track of where the bottom-most empty mailbox is. In the beginning, this will be the lowest mailbox (on the bottom of the stack). When we push an item onto our mailbox stack, we put it in the mailbox that is marked (which is the first empty mailbox), and move the marker up one mailbox. When we pop an item off the stack, we move the marker down one mailbox and remove the item from that mailbox. Anything below the marker is considered “on the stack”. Anything at the marker or above the marker is not on the stack.

The stack itself is a fixed-size chunk of memory addresses. The mailboxes are **memory addresses**, and the “items” we’re pushing and popping on the stack are called **stack frames**. A stack frame keeps track of all of the data associated with one function call. We’ll talk more about stack frames in a bit. The “marker” is a **register** (a small piece of memory in the CPU) known as the **stack pointer** (sometimes abbreviated “**SP**”). The stack pointer keeps track of where the top of the call stack currently is.

# Heap

The heap is a region of your computer's memory that is not managed automatically for you, and is not as tightly managed by the CPU.

[7.9 - The stack and the heap](https://www.learncpp.com/cpp-tutorial/79-the-stack-and-the-heap/)

[https://www.journaldev.com/4098/java-heap-space-vs-stack-memory](https://www.journaldev.com/4098/java-heap-space-vs-stack-memory)

[https://www.gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html](https://www.gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html)

[https://www.programmerinterview.com/index.php/data-structures/difference-between-stack-and-heap/](https://www.programmerinterview.com/index.php/data-structures/difference-between-stack-and-heap/)