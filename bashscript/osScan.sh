#!/bin/bash

echo -n "Please enter an ip address to scan for OS type: "; read ip
echo "Network range acquired successfully."
echo "Attempting OS scan on: " $ip
sudo nmap -O $ip > outputs/osscan.csv
echo "Look inside the outputs folder for scan result."