# POSIX

**POSIX (Portable Operating System Interface)** is a set of standard operating system interfaces based on the Unix operating system. It was specified by the IEEE committee in the 1980s.

# Origin of the name

> When the first part of the specification was ready, someone gave it the name "IEEEIX", with a subtitle that included "Portable Operating System". It seemed to me that nobody would ever say "IEEEIX". So I put the initials of "Portable Operating System" together with the same suffix "ix", and came up with "POSIX". It sounded good and I saw no reason not to use it, so I suggested it.

# Why Unix?

Unix was selected as the basis for a standard system interface partly because it was "manufacturer-neutral." However, several major versions of Unix existed so there was a need to develop a common denominator system.

# Specifications

Informally, each standard in the POSIX set is defined by a decimal following the POSIX. Thus, POSIX.1 is the standard for an application program interface in the C language. POSIX.2 is the standard shell and utility interface (that is to say, the user's command interface with the operating system).

## 1. C API

Greatly [extends ANSI C](https://stackoverflow.com/questions/9376837/difference-bewteen-c-standard-library-and-c-posix-library/37969420#37969420) with things like:

- More file operations:
    - `mkdir`, `dirname`, `symlink`, `readlink`, `link`(hardlinks), `[poll()](https://stackoverflow.com/questions/12444679/how-does-the-poll-c-linux-function-work/44127590#44127590)`, `stat`, `sync`, `[nftw()](https://stackoverflow.com/questions/8436841/how-to-recursively-list-directories-in-c-on-linux/29402705)`
- Process and threads:
    - `fork`, `execl`, `pipe`, semaphors `[sem_*](https://stackoverflow.com/questions/16400820/how-to-use-posix-semaphores-on-forked-processes-in-c/52042490#52042490)`, shared memory (`shm_*`), `kill`, scheduling parameters (`nice`, `sched_*`), `sleep`, `mkfifo`, `[setpgid()](https://stackoverflow.com/questions/6108953/how-does-ctrl-c-terminate-a-child-process/52042970#52042970)`
- networking: `[socket()](https://stackoverflow.com/questions/11208299/how-to-make-an-http-get-request-in-c-without-libcurl/35680609#35680609)`
- memory management: `mmap`, `mlock`, `mprotect`, `madvise`, `[brk()](https://stackoverflow.com/questions/6988487/what-does-the-brk-system-call-do/31082353#31082353)`
- utilities: regular expressions (`reg*`)

Those APIs also determine underlying system concepts on which they depend, e.g. `fork` requires a concept of a process.

Many [Linux system calls](https://unix.stackexchange.com/questions/421750/where-do-you-find-the-syscall-table-for-linux) exist to implement a specific POSIX C API function and make Linux compliant, e.g. `sys_write`, `sys_read`, ... Many of those syscalls also have Linux-specific extensions however.

Major Linux desktop implementation: glibc, which in many cases just provides a shallow wrapper to system calls.

## 2. Command Line Interface utilities

E.g.: `cd`, `ls`, `echo`, ...

Many utilities are direct shell front ends for a corresponding C API function, e.g. `mkdir`.

Major Linux desktop implementation: GNU Coreutils for the small ones, separate GNU projects for the big ones: `sed`, `grep`, `awk`, ... Some CLI utilities are implemented by Bash [as built-ins](https://unix.stackexchange.com/questions/11454/what-is-the-difference-between-a-builtin-command-and-one-that-is-not).

## 3. Shell language

E.g., `a=b; echo "$a"`

Major Linux desktop implementation: [GNU Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)).

## 4. Environment variables

E.g.: HOME, PATH.

## 5. Program exit status

ANSI C says `0` or `EXIT_SUCCESS` for success, `EXIT_FAILURE` for failure, and leaves the rest implementation to be defined.

POSIX adds:

- `126`: command found but not executable.
- `127`: command not found.
- `> 128`: terminated by a signal.

    But POSIX does not seem to specify the `128 + SIGNAL_ID` rule used by Bash: [https://unix.stackexchange.com/questions/99112/default-exit-code-when-process-is-terminated](https://unix.stackexchange.com/questions/99112/default-exit-code-when-process-is-terminated)

## 6. Regular expression

There are two types: BRE (Basic) and ERE (Extended). Basic is deprecated and only kept to not break APIs.

Those are implemented by C API functions, and used throughout CLI utilities, e.g. `grep` accepts BREs by default, and EREs with `-E`.

E.g.: `echo 'a.1' | grep -E 'a.[[:digit:]]'`

Major Linux implementation: glibc implements the functions under [regex.h](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/regex.h.html) which programs like `grep` can use as backend.

## 7. Directory structure

E.g.: `/dev/null`, `/tmp`

The Linux [FHS](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) greatly extends POSIX.

## 8. File names

- `/` is the path separator
- `NUL` cannot be used
- `.` is `cwd`, `..` parent
- portable filenames
    - use at most max 14 chars and 256 for the full path
    - can only contain: `a-zA-Z0-9._-`

## 9. Command line utility API conventions

Not mandatory, used by POSIX, but almost nowhere else, notably not in GNU. But true, it is too restrictive, e.g. single letter flags only (e.g. `-a`), no double hyphen long versions (e.g. `--all`).

A few widely used conventions:

- `-` means stdin where a file is expected
- `--` terminates flags, e.g. `ls -- -l` to list a directory named `-l`

# Reference

[What is 'x' in POSIX?](https://www.quora.com/What-is-x-in-POSIX)

[What is POSIX (Portable Operating System Interface)? - Definition from WhatIs.com](https://whatis.techtarget.com/definition/POSIX-Portable-Operating-System-Interface)

[What is the meaning of "POSIX"?](https://stackoverflow.com/questions/1780599/what-is-the-meaning-of-posix)