# Runlevel

A **runlevel** is one of the modes that a **Unix-based operating system** will run in. Each runlevel has a certain number of services stopped or started, giving the user control over the behavior of the machine. Conventionally, seven runlevels exist, numbered from zero to six.

[Runlevels](images/https://www.notion.so/70795d9091d748d48d82da3d964ce55f)

Runlevels 2-5 vary depending on distribution. For example, **on Ubuntu and Debian, runlevels 2-5 are the same and provide a full multi-user mode with networking and graphical login.** On Fedora and Red Hat, runlevel 2 provides multi-user mode without networking (console login only), runlevel 3 provides multi-user mode with networking (console login only), runlevel 4 is unused, and runlevel 5 provides multi-user mode with networking and graphical login.

One of the most common usages for single-user mode is to change the root password for a server on which the current password is unknown.

# Init program

**Init** (short for initialization) is the program on Unix and Unix-like systems that spawns all other processes. It runs as a daemon and typically has **PID 1**.

After the Linux kernel has booted, the **init program** reads the `/etc/inittab` file to determine the behavior for each runlevel. The applications that are started by init are located in the **`/etc/rc.d`** folder. Within this directory there is a separate folder for each run level, eg *`rc0.d`*, *`rc1.d`*, and so on.

![](Untitled-34d8220b-6121-4088-b461-1127a6223eee.png)

# `reboot`, `init 6`, `shutdown -r now`

There is no difference in them. Internally they do exactly the same thing.

# `telinit`, `init`

There is no difference. `telinit 5` and `init 5` executed from the command line will produce identical results.

# References

[what are init 0 init 1 init 2 init 3 init 4 init 5 init 6?](https://linuxonfire.wordpress.com/2012/10/19/what-are-init-0-init-1-init-2-init-3-init-4-init-5-init-6-2/)

[Linux Runlevels Explained | Liquid Web Knowledge Base](https://www.liquidweb.com/kb/linux-runlevels-explained/)

[What Are "Runlevels" on Linux?](https://www.howtogeek.com/119340/htg-explains-what-runlevels-are-on-linux-and-how-to-use-them/)

[Runlevel - Wikipedia](https://en.wikipedia.org/wiki/Runlevel)

[What is the difference between reboot , init 6 and shutdown -r now?](https://unix.stackexchange.com/questions/64280/what-is-the-difference-between-reboot-init-6-and-shutdown-r-now)

[telinit vs init](https://www.linuxquestions.org/questions/linux-newbie-8/telinit-vs-init-539578/)

[Runlevel 2 multitask or not?](https://www.notion.so/c25ef96412384ba2be7b335fa5b8de1e)