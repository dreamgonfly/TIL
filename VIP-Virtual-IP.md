# VIP (Virtual IP)

A virtual IP address (**VIP** or **VIPA**) is an IP address that doesn't correspond to an actual physical network interface. VIP maps traffic received at one IP address to another address based on port number.

![](images/-8c3f8aad-9a30-4bbb-bbd1-174db564d214untitled)

# Benefits

## Conservation of public IPs

A common application of VIPs is to have one public IP address represent the Web server, email server and FTP server, each of which has a unique private IP address. This sharing of one external IP address provides a good way to conserve public IP addresses.

## Security (port forwarding)

A Virtual IP can also be used for port forwarding. For example, assume you want to open web access to the Internet to a web server you have that is listening on port 80. However, due to security concerns, you only want users to be accessing this site using port 8080. You can use Virtual IP to accomplish this. Specify the Virtual IP, which is the IP address that the Internet will be using to access the web site. Then, specify the external port, and this combination of external IP and port will be mapped to an internal IP address and port.

## Availability

A virtual IP address eliminates a host's dependency upon individual network interfaces. Previously, if an interface failed, any connections to that interface were lost. With VIPA on your system and routing protocols within the network providing automatic reroute, recovery from failures occurs without disruption to the existing user connections that are using the virtual interface as long as packets can arrive through another physical interface. Systems running VIPA are more highly available because adapter outages no longer affect active connections. Because multiple physical adapters carry the system IP traffic, overall load is not concentrated on a single adapter and associated subnet.

# vs. Routers

Routers distribute packets based on their final destination. In contrast, VIP is the final destination and the traffic is distributed based on the port number.

# Reference

[Juniper Networks - [ScreenOS] What is a VIP used for?](https://kb.juniper.net/InfoCenter/index?page=content&id=KB5916)

[](https://www.juniper.net/documentation/software/screenos/screenos6.3.0/630_ce_AddressTranslation.pdf)

[](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/com.ibm.aix.networkcomm/tcpip_vipa_intro.htm)

[Virtual IP address - Wikipedia](https://en.wikipedia.org/wiki/Virtual_IP_address)