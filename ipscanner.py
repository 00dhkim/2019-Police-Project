import nmap

def scan(network_id):
	nm = nmap.PortScanner()
	res = nm.scan(hosts = network_id+'.0/24', arguments = '-sP')
	return res

def ip_print(res):
	ip_list = []
	for x in res['scan'].keys():
		list_tmp = [x]
		print(x, end='\t')
		try:
			print(list(res['scan'][x]['vendor'].keys())[0], list(res['scan'][x]['vendor'].values())[0], sep = '\t')
			list_tmp.append(list(res['scan'][x]['vendor'].keys())[0])
			list_tmp.append(list(res['scan'][x]['vendor'].values())[0])
		except:
			print()
		ip_list.append(list_tmp)
#	print(ip_list)
#	print(res)
	return ip_list

