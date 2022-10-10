#!/bin/bash

echo -n "Please specify port numbers to do port scan: "; read port
echo "Port range acquired successfully."
echo -n "Please enter a network range for port scan: "; read ip
echo "Network range acquired successfully."
echo "Attempting port scan on: " $port
sudo nmap -p $port $ip > outputs/portscan.csv
echo "Look inside the outputs folder for scan result."