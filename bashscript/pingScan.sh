#!/bin/bash

echo -n "Please enter an ip address to do a ping scan: "; read ip
echo "Network range acquired successfully."
echo "Attempting ping scan on: " $ip
sudo nmap -sn $ip > outputs/pingscan.csv
echo "Look inside the outputs folder for scan result."