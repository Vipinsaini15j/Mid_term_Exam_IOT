'''
Name: Vipin Saini
Subject: Internet of Things
Roll No: 24IMAI007
Question 1:


'''

# Answer:
# (1).
# For live video streaming from multiple cameras to the monitoring server, UDP is used. 
# Live streaming requires real-time communication with minimum delay delay. 
# UDP is faster because it is connectionless and does not perform acknowledgment, retransmission, or congestion control. 
# In video streaming, occasional packet loss is acceptable because missing frames do not significantly affect overall monitoring, 
# and retransmission would introduce delay. Therefore, UDP is more suitable for continuous, real-time video transmission.

# ----------------------------------------------------------------------------------------------------------------------------------

#(2).
# For transmitting critical alert notifications such as intrusion detection or fire detection, 
# TCP should be used. These alerts are safety-critical and must reach the control room without failure. 
# TCP ensures reliable data delivery through acknowledgments, retransmissions, sequencing, and error checking. 
# Even if packets are lost, TCP automatically retransmits them. 
# Although TCP may introduce slight delay due to connection establishment and error control mechanisms,
# reliability is more important than speed for critical alerts.

# ------------------------------------------------------------------------------------------------------------------------------------
# (3).
# In terms of reliability, TCP provides high reliability by guaranteeing delivery, maintaining order, and retransmitting lost packets. 
# UDP does not guarantee delivery, ordering, or duplication control. Therefore, TCP is suitable for critical alerts, 
# while UDP is acceptable for live streaming where perfect reliability is not mandatory.

# In terms of speed, UDP is faster because it has minimal overhead and no connection setup process. 
# TCP is slower due to its handshake process, acknowledgment mechanism, and congestion control.

# Regarding connection establishment, TCP is connection-oriented and uses a three-way handshake before transmitting data,
# ensuring a reliable session between sender and receiver.
# UDP is connectionless and sends data immediately without establishing a connection, reducing latency.

# For packet loss handling, TCP detects packet loss using sequence numbers and retransmits lost packets automatically,
#  ensuring complete delivery. UDP does not handle packet loss; 
# lost packets are not recovered unless managed at the application level. 
# In live video streaming, some packet loss is tolerable, but for critical alerts, 
# packet loss must be prevented through TCP’s retransmission mechanism.

#------------------------------------------------------------------------------------------------------------------------------------




