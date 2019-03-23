# Stack & Heap memory

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

## Properties

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

The heap is a region of your computer's memory that is not managed automatically for you, and is not as tightly managed by the CPU. It is a more free-floating region of memory (and is larger). 

To allocate memory on the heap, you must use **malloc()** or **calloc()**, which are built-in C functions. Once you have allocated memory on the heap, you are responsible for using **free()** to deallocate that memory once you don't need it any more. If you fail to do this, your program will have what is known as a **memory leak**. That is, memory on the heap will still be set aside (and won't be available to other processes).

## Properties

- variables can be accessed globally
- no limit on memory size
- (relatively) slower access
- no guaranteed efficient use of space, memory may become fragmented over time as blocks of memory are allocated, then freed
- you must manage memory (you're in charge of allocating and freeing variables)
- variables can be resized using `realloc()`

## Heap data structure

A heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C.

![](images/-9f3d0d07-6a20-4ea9-a698-d41260efbfebuntitled)

## Fragmentation

Fragmentation occurs when the available memory on the heap is being stored as noncontiguous (or disconnected) blocks – because used blocks of memory are in between the unused memory blocks. When excessive fragmentation occurs, allocating new memory may be impossible because of the fact that even though there is enough memory for the desired allocation, there may not be enough memory in one big block for the desired amount of memory.

# Example

## In Java

    package com.journaldev.test;
    
    public class Memory {
    
    	public static void main(String[] args) { // Line 1
    		int i=1; // Line 2
    		Object obj = new Object(); // Line 3
    		Memory mem = new Memory(); // Line 4
    		mem.foo(obj); // Line 5
    	} // Line 9
    
    	private void foo(Object param) { // Line 6
    		String str = param.toString(); //// Line 7
    		System.out.println(str);
    	} // Line 8
    
    }

![](images/-eb2e2e00-856b-48a7-8509-43375ce6d4c1untitled)

- As soon as we run the program, it loads all the Runtime classes into the Heap space. When main() method is found at line 1, Java Runtime creates stack memory to be used by main() method thread.
- We are creating primitive local variable at line 2, so it’s created and stored in the stack memory of main() method.
- Since we are creating an Object in line 3, it’s created in Heap memory and stack memory contains the reference for it. Similar process occurs when we create Memory object in line 4.
- Now when we call foo() method in line 5, a block in the top of the stack is created to be used by foo() method. Since Java is pass by value, a new reference to Object is created in the foo() stack block in line 6.
- A string is created in line 7, it goes in the [String Pool](https://www.journaldev.com/797/what-is-java-string-pool) in the heap space and a reference is created in the foo() stack space for it.
- foo() method is terminated in line 8, at this time memory block allocated for foo() in stack becomes free.
- In line 9, main() method terminates and the stack memory created for main() method is destroyed. Also the program ends at this line, hence Java Runtime frees all the memory and end the execution of the program.

## In C

An object can be stored either on the heap or on the stack.

### Code to create an object on the stack:

    void somefunction( )
    {
    /* create an object "m" of class Member
        this will be put on the stack since the 
        "new" keyword is not used, and we are 
       creating the object inside a function
    */
      
      Member m;
    
    } //the object "m" is destroyed once the function ends

So, the object “m” is destroyed once the function has run to completion

### Code to create an object on the heap:

    void somefunction( )
    {
    /* create an object "m" of class Member
        this will be put on the heap since the 
        "new" keyword is used, and we are 
       creating the object inside a function
    */
      
      Member* m = new Member( ) ;
      
      /* the object "m" must be deleted
          otherwise a memory leak occurs
      */
    
      delete m; 
    }

We must delete the “m” object on our own as well – otherwise we will end up with a memory leak.

# In multithreading

In a multi-threaded application, each thread will have its own stack. But, all the different threads will share the heap. This also means that there has to be some coordination between the threads so that they don’t try to access and manipulate the same piece(s) of memory in the heap at the same time.

# Reference

[7.9 - The stack and the heap](https://www.learncpp.com/cpp-tutorial/79-the-stack-and-the-heap/)

[Java Heap Space vs Stack - Memory Allocation in Java - JournalDev](https://www.journaldev.com/4098/java-heap-space-vs-stack-memory)

[7. Memory : Stack vs Heap](https://www.gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html)

[Difference between stack and heap - Programmer and Software Interview Questions and Answers](https://www.programmerinterview.com/index.php/data-structures/difference-between-stack-and-heap/)

[Heap (data structure) - Wikipedia](https://en.wikipedia.org/wiki/Heap_(data_structure))