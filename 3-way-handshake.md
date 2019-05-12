# 3-way handshake

To establish a connection, TCP uses a three-way [handshake](https://en.wikipedia.org/wiki/Handshaking). To establish a connection, the three-way (or 3-step) handshake occurs:

1. **SYN**: The client sends a SYN to the server. The client sets the segment's sequence number to a random value A.
2. **SYN-ACK**: In response, the server replies with a SYN-ACK. The acknowledgment number is set to one more than the received sequence number i.e. A+1, and the sequence number that the server chooses for the packet is another random number, B.
3. **ACK**: Finally, the client sends an ACK back to the server. The sequence number is set to the received acknowledgement value i.e. A+1, and the acknowledgement number is set to one more than the received sequence number i.e. B+1.

At this point, both the client and server have received an acknowledgment of the connection. The steps 1, 2 establish the connection parameter (sequence number) for one direction and it is acknowledged. The steps 2, 3 establish the connection parameter (sequence number) for the other direction and it is acknowledged.

![](images/Untitled-ee41806b-80de-4565-9b1d-baffaf71f089.png)

# Why do we need a 3-way handshake?

In TCP, the two parties keep track of what they have sent by using a **Sequence number**. Effectively it ends up being a running byte count of everything that was sent. The receiving party can use the opposite speaker's sequence number to acknowledge what it has received.

But the sequence number doesn't start at 0. It starts at the **ISN (Initial Sequence Number)**, which is a randomly chosen value. And since TCP is a bi-directional communication, both parties can "speak", and therefore both must randomly generate an ISN as their starting Sequence Number. Which in turn means, both parties need to notify the other party of their starting ISN.

3-way handshake actually consists of four events.

1. Alice picks an ISN and **SYNchronizes** it with Bob.
2. Bob **ACKnowledges** the ISN.
3. Bob picks an ISN and **SYNchronizes** it with Alice.
4. Alice **ACKnowledges** the ISN.

    Alice ---> Bob    SYNchronize with my Initial Sequence Number of X
    Alice <--- Bob    I received your syn, I ACKnowledge that I am ready for [X+1]
    Alice <--- Bob    SYNchronize with my Initial Sequence Number of Y
    Alice ---> Bob    I received your syn, I ACKnowledge that I am ready for [Y+1]

In actuality though, the middle two events (#2 and #3) happen in the same packet. What makes a packet a SYN or ACK is simply a binary flag turned on or off inside each TCP header, so there is nothing preventing both of these flags from being enabled on the same packet.

3-way handshake is actually 2-way handshake *in each direction*.

## Why do we need an ISN?

We need sequence numbers for retransmissions to work properly (or indeed at all). The ISN can't just be zero because of **sequence prediction attacks**.

# TCP Packets in action

Let's become more comfortable examining TCP sequence and acknowledgement numbers in the **Wireshark packet analyzer**.

![](images/Untitled-59da86ec-b251-4101-a9c8-8a1d8edba276.png)

The example capture contains a single HTTP request to a web server, in which the client web browser requests a single image file, and the server returns an HTTP/1.1 200 (OK) response which includes the file requested. You can right-click on any of the **TCP packets** within this capture and select **Follow TCP Stream** to open the raw contents of the TCP stream in a separate window for inspection. Traffic from the client is shown in red, and traffic from the server in blue.

## 3-way handshake

TCP utilizes a number of flags, or 1-bit boolean fields, in its header to control the state of a connection. The three we're most interested in here are:

- **SYN** - (Synchronize) Initiates a connection
- **FIN** - (Final) Cleanly terminates a connection
- **ACK** - Acknowledges received data

As we'll see, a packet can have multiple flags set.

Select packet #1 in Wireshark and expand the TCP layer analysis in the middle pane, and further expand the "Flags" field within the TCP header. Here we can see all of the TCP flags broken down. Note that the SYN flag is on (set to 1).

![](images/Untitled-565759e6-be06-448d-b6f3-d8b8d43ff4fe.png)

Now do the same for packet #2. Notice that it has two flags set: ACK to acknowledge the receipt of the client's SYN packet, and SYN to indicate that the server also wishes to establish a TCP connection.

![](images/Untitled-2fc95b7e-fc24-442a-a85a-e14362924b4e.png)

Packet #3, from the client, has only the ACK flag set. These three packets complete the initial TCP three-way handshake.

## Sequence and Acknowledgment Numbers

The client on either side of a TCP session maintains a **32-bit *sequence number*** it uses to keep track of how much data it has sent. This sequence number is included on each transmitted packet, and acknowledged by the opposite host as an ***acknowledgement number*** to inform the sending host that the transmitted data was received successfully.

When a host initiates a TCP session, its initial sequence number is effectively random; it may be any value between 0 and 4,294,967,295, inclusive. However, protocol analyzers like Wireshark will typically display ***relative* sequence and acknowledgement numbers** in place of the actual values. These numbers are relative to the initial sequence number of that stream. This is handy, as it is much easier to keep track of relatively small, predictable numbers rather than the actual numbers sent on the wire.

For example, the initial relative sequence number shown in packet #1 is 0 (naturally), while the ASCII decode in the third pane shows that the actual sequence number is 0xf61c6cbe, or 4129057982 decimal.

![](images/Untitled-081baa24-ce38-4180-b8fa-089e929458fb.png)

To better understand how sequence and acknowledgement numbers are used throughout the duration of a TCP session, we can utilize Wireshark's built-in flow graphing ability. Navigate to Statistics > Flow Graph..., select TCP flow and click OK. Wireshark automatically builds a graphical summary of the TCP flow.

![](images/Untitled-4769bc55-e96a-47ff-bdd2-0974745365fa.png)

Each row represents a single **TCP packet**. The left column indicates **the direction of the packet, TCP ports, segment length, and the flag(s) set**. The column at right lists **the relative sequence and acknowledgement numbers** in decimal. Selecting a row in this column also highlights the corresponding packet in the main window.

We can use this flow graph to better understand how sequence and acknowledgement numbers work.

### **Packet #1**

Each side of a TCP session starts out with a (relative) sequence number of zero. Likewise, the acknowledgement number is also zero, as there is not yet a complementary side of the conversation to acknowledge.

(Note: The version of Wireshark used for this demonstration, 1.2.7, shows the acknowledgement number as an apparently random number. This believed to be a software bug; the initial acknowledgement number of a session should always be zero, as you can see from inspecting the hex dump of the packet.)

### **Packet #2**

The server responds to the client with a sequence number of zero, as this is its first packet in this TCP session, and a relative acknowledgement number of 1. **The acknowledgement number is set to 1 to indicate the receipt of the client's SYN flag in packet #1**.

Notice that the acknowledgement number has been increased by 1 although no payload data has yet been sent by the client. This is because the presence of the SYN or FIN flag in a received packet triggers an increase of 1 in the sequence. (This does not interfere with the accounting of payload data, because packets with the SYN or FIN flag set do not carry a payload.)

### **Packet #3**

Like in packet #2, the client responds to the server's sequence number of zero with an acknowledgement number of 1. The client includes its own sequence number of 1 (incremented from zero because of the SYN).

At this point, the sequence number for both hosts is 1. This initial increment of 1 on both hosts' sequence numbers occurs during the establishment of all TCP sessions.

### **Packet #4**

This is the first packet in the stream which carries an actual payload (specifically, the client's HTTP request). The sequence number is left at 1, since no data has been transmitted since the last packet in this stream. The acknowledgement number is also left at 1, since no data has been received from the server, either.

Note that this packet's payload is 725 bytes in length.

### **Packet #5**

This packet is sent by the server solely to acknowledge the data sent by the client in packet #4 while upper layers process the HTTP request. Notice that the acknowledgement number has increased by 725 (the length of the payload in packet #4) to 726; e.g., "I have received 726 bytes so far." The server's sequence number remains at 1.

### **Packet #6**

This packet marks the beginning of the server's HTTP response. Its sequence number is still 1, since none of its packets prior to this one have carried a payload. This packet carries a payload of 1448 bytes.

### **Packet #7**

The sequence number of the client has been increased to 726 because of the last packet it sent. Having received 1448 bytes of data from the server, the client increases its acknowledgement number from 1 to 1449.

For the majority of the capture, we will see this cycle repeat. The client's sequence number will remain steady at 726, because it has no data to transmit beyond the initial 725 byte request. The server's sequence number, in contrast, continues to grow as it sends more segments of the HTTP response.

# **Tear-down**

### **Packet #38**

After acknowledging the last segment of data from the server, the client processes the HTTP response as a whole and decides no further communication is needed. Packet #38 is sent by the client with the FIN flag set. Its acknowledgement number remains the same as in the prior packet (#37).

### **Packet #39**

The server acknowledges the client's desire to terminate the connection by increasing the acknowledgement number by one (similar to what was done in packet #2 to acknowledge the SYN flag) and setting the FIN flag as well.

### **Packet #40**

The client sends its final sequence number of 727, and acknowledges the server's FIN packet by incrementing the acknowledgement number by 1 to 22952.

At this point, both hosts have terminated the session and can release the software resources dedicated to its maintenance.

# Reference

[Transmission Control Protocol - Wikipedia](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment)

[Why do we need a 3-way handshake? Why not just 2-way?](https://networkengineering.stackexchange.com/questions/24068/why-do-we-need-a-3-way-handshake-why-not-just-2-way)

[What Is a Three-Way Handshake in TCP?](https://www.youtube.com/watch?v=LyDqA-dAPW4)

[Understanding TCP Sequence and Acknowledgment Numbers - PacketLife.net](http://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/)