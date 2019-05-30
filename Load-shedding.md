# Load shedding

**Load Shedding** is a technique used in information systems, especially web services, to avoid overloading the system and making it unavailable for all users. The idea is to ignore some requests rather than crashing a system and making it fail to serve any request.

# Considerations

Considerations shaping the design of load shedding algorithms include:

- when one of several [load balanced](https://en.wikipedia.org/wiki/Load_balancing_(computing)) servers becomes unavailable due to overload, all other servers will receive a higher load, potentially leading to more overload and a snow-ball effect which takes down the entire system.
- when one part in a system of [microservices](https://en.wikipedia.org/wiki/Microservices) starts becoming slower due to high load, other services will have waiting requests queuing up, potentially more than fits in their memory, which could again take down the entire system.

# Reference

[Load Shedding - Wikipedia](https://en.wikipedia.org/wiki/Load_Shedding)