

import os
import sys
import subprocess


      

print ("##################################################################################################################")
print ("# Welcome to DiscoAttack #")
print ("This tool is a prototype for Discovering, Testing the vulnerabilities, and analysing of the packets.\nThe Intention of this tool is only and only educational.")
print ("Thank you for using this tool.")
print ("##################################################################################################################\n")

# Main services.
print ("##################################################################################################################")
print ("Services: discoverNetwork, listenNetwork, attackNetwork, exit")
print ("##################################################################################################################\n")


# User input for selecting the main service such as discoverNetwork, attackNetwork, or exit.
networkInput = input("Please specify a service to start: ")

# This function controls the user input regarding network discovery/ discoverNetwork.
# It contains all nmap scanning functions.
def discoverNetwork():
  # Outputs the selected service.
  print (networkInput, "selected. \n")
  print ("Searching for Nmap...")

  # Try block check if Nmap is installed on the system or not, if installed it shows the version of Nmap.
  # Except block warns for the absence of Nmap, and offers the user to install it. If the user decides not to install Nmap, the programme gets terminated.
  try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen("nmap", stdout=null, stderr=null)
    null.close()
    os.system("nmap --version")
    print ("Nmap found successfully!\n")
  except OSError:
    installNmap = input("Nmap not found, would you like to install it (y/n): ")
    if installNmap in ["y", "Y", "yes", "Yes", "YES"]:
      os.system("sudo apt install nmap")
      print ("Nmap successfully installed!\n")
    else:
      sys.exit("Nmap was not installed, DiscoAttack terminated!") 

  # Sub-services of discoverNetwork.
  print ("##################################################################################################################")
  print ("Scan type: pingScan, osScan, advancedScan, portScan, udpScan, synackScan, exit")
  print ("##################################################################################################################\n")

  # The user defines the type of scan they want to perform by typing form the list of discoverNetwork sub-services. 
  userInput = input("Please specify the type of scanning: ")

  
  def pingScan():
    # This function performs a ping scan, sends the output to outputs repo in .csv format.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/pingScan.sh')


  def osScan():
    # This function performs an OS scan, the output is send to the outputs repo.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/osScan.sh')

 
  def advancedScan():
    # This function preforms an Advanced scan, the output is send to the outputs repo.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/advancedScan.sh') 


  def portScan():
    # This function performs a Port scan, the output is send to the outputs repo.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/portScan.sh')  


  def udpScan():
    # This function performs a UDP scan, the output is send to the outputs repo.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/udpScan.sh')


  def synackScan():
    # This function performs a SYN/ACK scan function, the output is send to the outputs repo.
    print (userInput, "selected.\n")
    subprocess.call('bashscript/synackScan.sh')


  # Check the input for discoverNetwork sub-services and calls a function if matches with the input.
  if userInput == "pingScan":
    pingScan()
  elif userInput == "osScan":
    osScan()
  elif userInput == "advancedScan":
    advancedScan()
  elif userInput == "portScan":
    portScan()
  elif userInput == "udpScan":
    udpScan()
  elif userInput == "synackScan":
    synackScan()
  elif userInput == "exit":
    sys.exit("Terminated by user!")
  else:
    os.system("clear")
    print ("Invalid scan type! \n")
    discoverNetwork()



# This function is for listening to a specific network. It asks for a host IP address and starts capturing packets with tcpdump.
def listenNetwork():
  print (networkInput, "selected. \n")
  print ("Searching for tcpdump...") 

  # Try block check if tcpdump, is installed on the system or not, if installed it shows the version of Nmap.
  # Except block warns for the absence of tcpdump, and offers the user to install it. If the user decides not to install tcpdump, the programme gets terminated.      
  try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen("tcpdump", stdout=null, stderr=null)
    null.close()
    os.system("tcpdump --version")
    print ("tcpdump found successfully!\n")
  except OSError:
    installTcpDump = input("tcpdump not found, would you like to install it (y/n): ")
    if installTcpDump in ["y", "Y", "yes", "Yes", "YES"]:
      os.system("sudo apt install tcpdump")
      print ("tcpdump successfully installed!\n")
      os.system("tcpdump --version")
      print ("\n")
    else:
      sys.exit("tcpdump was not installed, DiscoAttack terminated!") 



   # Sub-services of listen network.
  print ("##################################################################################################################")
  print ("Sub-services: captureTraffic, exit")
  print ("##################################################################################################################\n")

  captureInput = input ("Please enter an input: ")

  def captureTraffic():
    # This function performs a UDP scan, the output is send to the outputs repo.
    print (captureInput, "selected.\n")
    subprocess.call('bashscript/captureNetwork.sh')




  if captureInput == "captureTraffic":
    captureTraffic()
  elif captureInput == "exit":
    sys.exit("Terminated by user!")
  else:
    os.system("clear")
    print ("Invalid scan type! \n")
    listenNetwork()



# This function attacks to specific network, It asks the user to enter an IP address and performs DDOS/DOS attack.
# hping3 is used for performing attacks.
def attackNetwork():
  print (networkInput, "selected. \n")
  print ("Searching for hping3...")

  # Try block check if hping3 is installed on the system or not, if installed it shows the version of hping3.
  # Except block warns for the absence of hping3, and offers the user to install it. If the user decides not to install hping3, the programme gets terminated.
  try:
    # pipe output to /dev/null for silence
    null = open("/dev/null", "w")
    subprocess.Popen("hping3", stdout=null, stderr=null)
    null.close()
    os.system("hping3 --version")
    print ("hping3 found successfully!\n")
  except OSError:
    installNmap = input("hping3 not found, would you like to install it (y/n): ")
    if installNmap in ["y", "Y", "yes", "Yes", "YES"]:
      os.system("sudo apt install hping3")
      print ("hping3 successfully installed!\n")
    else:
      sys.exit("hping3 was not installed, DiscoAttack terminated!")


  # Sub-services of attack network.
  print ("##################################################################################################################")
  print ("Sub-services: floodAttack, exit")
  print ("##################################################################################################################\n")    

  attackInput = input("Please specify a sub-service you want to use: ")    
  
  def floodAttack():
    # This function performs a flood attack.
    print (attackInput, "selected. \n")
    subprocess.call('bashscript/floodAttack.sh')



  if attackInput == "floodAttack":
    floodAttack()
  elif attackInput == "exit":
    sys.exit("Terminated by user!")
  else:
    sys.exit("Wrong input, DiscoAttack Terminated!")
      


# Controls the main services, checks if a user wants to scan a network or attack or exit.
if networkInput == "discoverNetwork":
  discoverNetwork()
elif networkInput == "listenNetwork":
  listenNetwork()
elif networkInput == "attackNetwork":
  attackNetwork()
elif networkInput == "exit":
  sys.exit("Terminated by user!")
else:
  sys.exit("Wrong input, DiscoAttack Terminated!")
  
