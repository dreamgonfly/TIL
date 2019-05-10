# Postel's law

Postel's Law, also known as **robustness principle** is a design guideline for software:

> Be conservative in what you do, be liberal in what you accept from others.

It is often reworded as:

> Be conservative in what you send, be liberal in what you accept.

This principle is named after Jon Postel, who wrote in an early specification of TCP.

![](images/Untitled-5413a785-e7ce-4a71-b4af-cf2bc0e0a3a6.png)

# Interpretation

Programs that send messages to other machines (or to other programs on the same machine) should conform completely to the specifications, but programs that receive messages should accept non-conformant input as long as the meaning is clear.

# Criticism

A defective implementation that sends non-conforming messages might be used only with implementations that tolerate those deviations from the specification until, possibly several years later, it is connected with a less tolerant application that rejects its messages. In such a situation, identifying the problem is often difficult, and deploying a solution can be costly. Rose therefore recommended "explicit consistency checks in a protocol ... even if they impose implementation overhead".

It is also argued that Postel's law leads to security problems.

# Reference

[Robustness principle - Wikipedia](https://en.wikipedia.org/wiki/Robustness_principle)

[Designing for rapid release - Crash & Burn 2012](https://www.slideshare.net/spnewman/designing-for-rapid-release/38-Postels_Law_Be_conservative_in)