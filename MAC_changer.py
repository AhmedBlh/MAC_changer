#   NB: this code requires super user privileges : -- run with sudo --  
#   _____ 1/ Change the MAC address manually_____

#   Disable the interface: ifconfig [your interface: eth0, wlan0 ...] down
#   Change the address: ifconfig [your interface: eth0, wlan0 ...] hw ether [the new MAC address: 00:00:00:00:00:00:00:00]
#   Enable the interface again: ifconfig eth0 up

#   _____ 2/ Change the MAC address using the subprocess module_____

from ast import arguments
from pickletools import optimize
import subprocess
import optparse

from click import option

def mac_changer(interface,new_mac):
    print(' --- Changing MAC for '+ interface + ' to the address ' + new_mac)
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

#   _____ 2.1/ Put here your information (interface and MAC) Manually : sudo python MAC_changer.py _____ 

#interface = 'eth0'
#new_mac =  '00:11:22:33:44:55'
#mac_changer(interface, new_mac)

#   _____ 2.2/ Get the input from the user {Python2 Version} : the difference resides in (input > raw_input) 

#   _____ 2.2.1/ Using Arguments : sudo python MAC_changer.py -i eth0 -a 00:11:22:33:44:55____ 

#def get_arguments():
#    parser = optparse.OptionParser()
#    parser.add_option('-i', '--interface', dest='interface', help='The interface you want to modify')
#    parser.add_option('-a', '--address', dest='new_mac', help='The new MAC address ')
#    return parser.parse_args()

#(options, arguments) = get_arguments()
#mac_changer(options.interface, options.new_mac)

# ______ 2.2.2/ Using command prompt : sudo python MAC_changer.py _____ 

#interface = raw_input ('interface [Ex: eth0] : ')
#new_mac =  raw_input ('MAC address [Ex: 00:11:22:33:44:55] : ')
#mac_changer(interface, new_mac)

#   _____ 2.3/ Get the input from the user {Python3 Version} : sudo python MAC_changer.py _____

#interface = input ('interface [Ex: eth0] : ')
#new_mac =  input ('MAC address [Ex: 00:11:22:33:44:55] : ')
#mac_changer(interface,new_mac)
