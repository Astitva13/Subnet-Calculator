import ipaddress

def subnet_calculator(ip_cidr):
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
        hosts = list(network.hosts())
        print(f"\nSubnet Calculator Results for {ip_cidr}\n")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"CIDR Notation: /{network.prefixlen}")
        print(f"Number of Usable Hosts: {len(hosts)}")
        if hosts:
            print(f"First Usable IP: {hosts[0]}")
            print(f"Last Usable IP: {hosts[-1]}")
        print("\n")
    except ValueError:
        print("Invalid IP/CIDR. Please enter a valid value (e.g., 192.168.1.10/24)")

if __name__ == "__main__":
    ip_cidr = input("Enter IP address with CIDR (e.g., 192.168.1.10/24): ")
    subnet_calculator(ip_cidr)
