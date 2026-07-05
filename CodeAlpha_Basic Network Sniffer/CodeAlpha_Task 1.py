Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from scapy.all import sniff, IP, TCP, UDP, ICMP
... 
... def packet_callback(packet):
... 
...     if packet.haslayer(IP):
... 
...         src_ip = packet[IP].src
...         dst_ip = packet[IP].dst
... 
...         protocol = "Other"
... 
...         if packet.haslayer(TCP):
...             protocol = "TCP"
...         elif packet.haslayer(UDP):
...             protocol = "UDP"
...         elif packet.haslayer(ICMP):
...             protocol = "ICMP"
... 
...         print("\n--------------------------------------")
...         print(f"Source IP      : {src_ip}")
...         print(f"Destination IP : {dst_ip}")
...         print(f"Protocol       : {protocol}")
... 
...         if packet.payload:
...             payload = bytes(packet.payload)
... 
...             try:
...                 print(f"Payload        : {payload[:50].decode('utf-8', errors='ignore')}")
...             except:
...                 print("Payload        : Unable to decode")
... 
...         print("--------------------------------------")
... 
... print("Starting Network Packet Sniffer...")
... print("Capturing 20 packets...\n")
... 
... sniff(prn=packet_callback, store=False, count=20)
... 
