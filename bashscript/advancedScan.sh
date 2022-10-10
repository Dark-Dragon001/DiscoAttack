#!/bin/bash

echo -n "Please enter an ip address to do an advanced scan: "; read ip
echo "Network range acquired successfully."
echo "Attempting advanced scan on: " $ip
sudo nmap -A $ip > outputs/advancedscan.csv
echo "Look inside the outputs folder for scan result."