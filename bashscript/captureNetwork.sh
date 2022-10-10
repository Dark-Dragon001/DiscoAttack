#!/bin/bash

echo -n "Please enter an ip address to capture packets from: "; read ip
echo "Network range acquired successfully."
echo "tcpdump is going to capture 1000 packets from the given ip address. Please wait!"
echo ""
echo "Capturing packets form: " $ip
sudo tcpdump -i any host $ip -c 30 -w ./outputs/packets.pcap
echo "Look inside the outputs folder for scan result."