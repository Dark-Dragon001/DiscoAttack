#!/bin/bash

echo -n "Please enter an ip address to do a udp scan: "; read ip
echo "Network range acquired successfully."
echo "Attempting udp scan on: " $ip
sudo nmap -sU $ip > outputs/udpscan.csv
echo "Look inside the outputs folder for scan result."