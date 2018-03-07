import pyshark

def main():
	cap = pyshark.FileCapture("/path/to/pcap")
  #Dictionary that will store the websites as well as how many times it was queried
	websites = {}
	for packet in cap:
		if 'DNS' in packet:
			packetDNS = packet.dns.qry_name
			if packetDNS in websites:
				websites[packetDNS] += 1
			else:
				websites[packetDNS] = 1
       
main()
