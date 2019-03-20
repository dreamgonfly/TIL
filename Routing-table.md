# Routing table

A routing table is a set of rules, often viewed in table format, that is used to determine where data packets traveling over an Internet Protocol (IP) network will be directed. All IP-enabled devices, including routers and switches, use routing tables.

> Routing table shows all the routes that you can take.

![](images/-ea6c1e2e-07bc-43a1-a18f-9951b3bd9f8auntitled)

# Columns

## Destination

The IP address of the packet's final destination

## Gateway

The IP address of the gateway or the router to which the packet is forwarded.

> A router connects one network to another. A router is a gateway to another network. It is a door to another network.

## Genmask

The subnet mask for the destination net.

## Flags

- U: Up - Route is up and running.
- G: Gateway - Route is to a gateway router rather than to a directly connected network or host
- H: Host name - Route is to a host rather than to a network, where the destination address is a complete address

## Metric

Distance or cost to each available route so that the most cost-effective path can be chosen

## Iface

The outgoing network interface the device should use when forwarding the packet to the next hop or final destination

# Rows

## default

If a destination doesn't match any route the default rule is followed.

## asterisk

Asterisk on the gateway column means that the device is on the same network.

## Multiple matches

A packet' destination ip address is first compared to every route within a routing table. If it matches more than one rule, the one with longest subnet mask is chosen. IP address `192.168.0.15` follows the second rule because `192.168.0.15/24` of the second rule is longer than `192.168.0.15/0` of the first default rule.

# Reference

[https://www.youtube.com/watch?v=g8eP4fhrx3I](https://www.youtube.com/watch?v=g8eP4fhrx3I)

[What is routing table? - Definition from WhatIs.com](https://searchnetworking.techtarget.com/definition/routing-table)

[Routing table flags](https://library.netapp.com/ecmdocs/ECMP1155586/html/GUID-07F1F043-7AB7-4749-8F8D-727929233E62.html)