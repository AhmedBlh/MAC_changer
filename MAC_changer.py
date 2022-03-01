#   NB: this code requires super user privileges : -- run with sudo --  
#   _____Change the MAC address manually_____

#   Disable the interface: ifconfig [your interface: eth0, wlan0 ...] down
#   Change the address: ifconfig [your interface: eth0, wlan0 ...] hw ether [the new MAC address: 00:00:00:00:00:00:00:00]
#   Enable the interface again: ifconfig eth0 up

#   _____Change the MAC address using the subprocess module_____

from ast import arguments
from pickletools import optimize
import subprocess
import optparse

#   Put here your information (interface and MAC) Manually

#interface = 'eth0'
#new_mac =  '00:11:22:33:44:55'

#   _____ Get the input from the user {Python2 Version} : sudo python MAC_changer.py _____ 98:e7:f4:db:dc:53

#   _____ Using Arguments ____ 

#parser = optparse.OptionParser()
#parser.add_option('-i', '--interface', dest='interface', help='The interface you want to modify')
#parser.add_option('-a', '--address', dest='new_mac', help='The new MAC address ')
#(options, arguments) = parser.parse_args()
#interface= options.interface
#new_mac=options.new_mac

# ______ Using command prompt ______

interface = raw_input ('interface [Ex: eth0] : ')
new_mac =  raw_input ('MAC address [Ex: 00:11:22:33:44:55] : ')

#   _____ Get the input from the user {Python3 Version} : sudo python MAC_changer.py _____

#interface = input ('interface [Ex: eth0] : ')
#new_mac =  input ('MAC address [Ex: 00:11:22:33:44:55] : ')

def mac_changer(interface,new_mac):
    print(' --- Changing MAC for '+ interface + ' to the address ' + new_mac)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

mac_changer(interface,new_mac)