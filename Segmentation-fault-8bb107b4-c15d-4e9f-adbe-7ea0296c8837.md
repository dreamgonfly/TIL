# Segmentation fault

Segmentation fault or **segfault** is a specific kind of error caused by accessing memory that “does not belong to you.” Segfaults are caused by a program trying to read or write an illegal memory location. They are often associated with a file named **core.**

![](-f7e70257-745c-4efc-881b-44af0dc1f911untitled)

## Memory segments (reviewed)

Program memory is divided into different segments: a text segment for program instructions, a data segment for variables and arrays defined at compile time, a stack segment for temporary (or automatic) variables defined in subroutines and functions, and a heap segment for variables allocated during runtime by functions, such as malloc (in C) and allocate (in Fortran)

## Segfault related to memory segments

A segfault occurs when a reference to a variable falls outside the segment where that variable resides, or when a write is attempted to a location that is in a read-only segment. In practice, segfaults are almost always due to trying to read or write a non-existent array element, not properly defining a pointer before using it, or (in C programs) accidentally using a variable's value as an address

# Examples

## By dereferencing a null pointer

    int *p = NULL;
    *p = 1;

## By trying to write to a portion of memory that was marked as read-only

    char *str = "Foo"; // Compiler marks the constant string as read-only
    *str = 'b'; // Which means this is illegal and results in a segfault

## By dangling pointer points to a thing that does not exist any more

The pointer p dangles because it points to character variable c that ceased to exist after the block ended. And when you try to dereference dangling pointer (like *p='A'), you would probably get a segfault.

    char *p = NULL;
    {
        char c;
        p = &c;
    }
    // Now p is dangling

> This one is particularly nasty, when I build: int main() { char *p = 0; { char c = 'x'; p = &c; } printf( "%c\n",*p); return 0; } With either gcc or several other compilers, it 'appears' to work. No warnings on compile. No segfault. This is because the '}' out of scope, doesn't actually delete the data, just marks it as free to be used again. The code can run fine on a production system for years, you alter another part of the code, change compiler or something else and BOOOOOM!

# Reference

[What is a segmentation fault?](https://stackoverflow.com/questions/2346806/what-is-a-segmentation-fault)

[What is a segmentation fault?](https://stackoverflow.com/questions/2346806/what-is-a-segmentation-fault)