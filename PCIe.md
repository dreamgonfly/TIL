# PCIe

PCIe (Peripheral Component Interconnect express) is an interface standard for plugging modern expansion cards into modern motherboards.

There are two components: PCIe cards and PCIe slots.

![](images/-8a216087-70a5-4222-a3fb-36b4b6c4eb69untitled)

# Universality

PCIe works with pretty much any computer components (unlike older standards such as PCI, PCI-X, AGP), including graphics cards, sound cards, hard drives, SSDs, Wi-Fi and Ethernet hardware connections. AGP was only for graphics cards and PCI was for everything else.

# Physical configurations

PCIe slots come in different physical configurations: x1, x4, x8, x16, x32. The number after the x tells you how many lanes (how data travels to and from the PCIe card) that PCIe slot has. A PCIe x1 slot has one lane and can move data at one bit per cycle. A PCIe x2 slot has two lanes and can move data at two bits per cycle (and so on).

![](images/-1a1e66e7-7574-41c1-8281-14256f55de98untitled)

# Generations

All generations physically look the same on the connectors. However, the actual available bandwidth has doubled each generation. PCIe 3.0 achieves twice the speed of PCIe 2.0, and PCIe 2.0 achieves twice the speed of PCIe 1.0.

![](images/-38e1a2ba-042e-42a4-a729-34b056ef2b79untitled)

# Compatibility

- PCIe slots are upwards and downwards compatible. You can plug a PCIe 1x card into a 16x slot. It gets the same power delivery. It just gets less bandwidth delivered to it. Also, you can plug a 8x card into 4x slot. It'll still work but it will only have half of the bandwidth available.
- PCIe slots are compatible across generations, because they physically look the same.
- Performance is to be dictated by whatever is the lowest of the two components.

# Reference

[PCI Express (PCIe) 3.0 - Everything you Need to Know As Fast As Possible](https://youtu.be/LSSHuMHbCWo)

[PCI Express - Wikipedia](https://en.wikipedia.org/wiki/PCI_Express)

## Photo credit

[https://docs.oracle.com/cd/E62159_01/html/E62171/z40007611438967.html#scrolltoc](https://docs.oracle.com/cd/E62159_01/html/E62171/z40007611438967.html#scrolltoc)

[https://www.tomshardware.com/reviews/pcie-definition,5754.html](https://www.tomshardware.com/reviews/pcie-definition,5754.html)