#!/bin/bash

echo -n "Please enter an ip address to do a SYN/ACK scan: "; read ip
echo "Network range acquired successfully."
echo "Attempting SYN/ACK scan on: " $ip
sudo nmap -sS $ip > outputs/synackscan.csv
echo "Look inside the outputs folder for scan result."