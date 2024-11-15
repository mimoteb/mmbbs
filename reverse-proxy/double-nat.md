### Double Natting (2 firewalls)
The host machine is having multiple interfaces, wlan0 is the gateway and dhcp-enabled, vmnet8 is not showing any ip in the ip a command.
in the host machine there is a lab environment all the machines are virtualized, the fw (vm) is the firewall and has two main interfaces,
the eth0 of the virtualized firewall is the gateway for all the virtual machines and has dhcp enabled.
eth1 of the virtualized firewall has a static ip (192.168.199.254/24) and acts as a lan interface and a gateway for all vms,
both host machine and the virtualized firewall have iptables as a firewall.
the incoming packets that are hitting the wlan0 of the host machine and only the following ports (443, 4000:4003) should be,
forwarded to the lab environment machines like so:
incoming packets via wlan0 should forwarded as following:
|port|vm|vm-port|vm-name|
|---|---|---|---|
|443|192.168.199.100|443|reverse proxy server|
|4000|192.168.199.100|22|reverse proxy server|
|4001|192.168.199.101|22|web01|
|4002|192.168.199.102|22|web02|
|4003|192.168.199.103|22|web03|

Both firewalls (host machine and the virtualized firewall) should be able to 
handle the packets coming in wlan0 to their destination vms and proper ports.
host machine (dhcp) ip address is : 172.20.157.177/16
firewall (bridged) eth0 ip address is : 172.20.183.107/16
# Double NAT
### First phase of NAT (packets hitting external physicall iface i.e. wlan0)
```
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 4000 -j DNAT --to-destination <FW_IP>:4000
iptables -A FORWARD -i wlan0 -o vmnet8 -p tcp --dport 4000 -d <FW_IP> -j ACCEPT
iptables --insert INPUT --protocol tcp --dport 4000 --jump ACCEPT
```
### Second phase of NAT (packets hitting Firewall in the virtual Lab env.)
```
iptables -A FORWARD -p tcp -d <VM_IP> --dport 22 -j ACCEPT
```
# Proxy Server Logical topology
|vm|ip|ssh-port|username|password|
|---|---|---|---|---|
|**proxy**|192.168.199.**100**|4000|root|toor|
|**web01**|192.168.199.**101**|4001|root|toor|
|**web02**|192.168.199.**102**|4002|root|toor|
|**web03**|192.168.199.**103**|4003|root|toor|
