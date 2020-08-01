#! /usr/bin/python
import os 
import time
import sys
import subprocess
import socket
from contextlib import closing

#VARIABLES
print('Hello and Welcome, please insert your imput for the automation to start')
first = input('Start Automation ? (yes/no) ')
pleasure = 'It was a pleasure to work with you :)'


#LINKS LIBRARY
def suggestions():
    links = ('WebSec Resource: https://www.hacker101.com/resources.html', 'Wordlist: https://github.com/danielmiessler/SecLists',)
    if resource == "yes":
        
        for index,links in enumerate(links, start=1):
            print('The following suggestions are:')
            print(index, links) 
    else:
        print(pleasure)


#MAIN
if first == 'yes': #FIRST VERIFICATION (1)
    ip = input(str('Do you have the target ip, if so what is it, otherwise "press enter" to proceed '))
    url = input('Provide url of website, otherwise "press enter" to proceed ')
    resource = input('Would you like some resource suggestion to display in the end of the script ? (yes/no) ')

    def whatweb(): #START WHATWEB (6)
        if url == '':
            suggestions()
        else:
            subprocess.run(f'whatweb {url} > whatwebScan.txt', shell=True)
            suggestions()

    def metasploit(): #START METASPLOIT (5)
        meta = input('Would You like to start metasploit ? (yes/no) ')

        if meta == 'yes':
            subprocess.call(['gnome-terminal', '-x', 'msfconsole -q'])
            whatweb()

        else:
            whatweb()
              

    def nikto(): #START NIKTO (3)
        
        try:
            with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                if sock.connect_ex((ip, 80)) == 0:
                    nikto_response = input(f'It seems like that Port 80 from {ip} is open, would you like to use nikto ? (yes/no) ')
                    if nikto_response == 'yes':
                        subprocess.run(f'nikto -host {ip} -p 80 > niktoScan.txt', shell=True)

                    else:
                        metasploit()
                        

                else:
                    print ("Port 80 is closed")
                    print ("Skipping nikto...")
                    metasploit()
                   
        except:
            print('It seems like that the ip address is invalid make sure to verify it')
            


    if first == 'yes': #START NMAP (2)
        print('Starting nmap...')
        nmap_mode = input('NMAP (agressive/stealth/all/skip) ')

        if nmap_mode == 'agressive':
            print('Start scanning aggressively...')
            time.sleep(3)
            subprocess.run(f'nmap -A -T4 {ip} > nmapScan.txt', shell=True)
            nikto()

        elif nmap_mode == 'stealth':
            print('Start scanning stealth...')
            time.sleep(3)
            subprocess.run(f'nmap -T4 -sS -sV -O {ip} > nmapScan.txt', shell=True)
            nikto()

        elif nmap_mode == "all":
            print('Starting scanning everything possible...')
            time.sleep(3)
            subprocess.run(f'nmap -a -p- {ip} > nmapScan.txt')
            nikto()

            
        else:
            print('Checking if port 80 is open...')
            nikto()


else:
    exit()




