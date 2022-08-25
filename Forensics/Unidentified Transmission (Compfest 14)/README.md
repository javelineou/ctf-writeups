Title: Unidentified Transmission <br>
Description: I heard some eerie noises when I was streaming. I wonder what it is <br>

It can be seen from the packets, lots of UDP along with RTCP packets. These RTCP packets indirectly indicates the presence of traffic from RTP / RTSP. This can be proven by doing type-casting on the UDP protocol as RTP. <br>
Analyze > select Enabled Protocols > Search for RTP > Tick 'rtp_udp' <br>
Then export the RTP to audio file. The SSTV audio can be converted to image with SSTV decoder (Robot36) <br><br>


Flag: COMPFEST14{*******}
