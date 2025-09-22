import ipaddress
import tkinter as tk
from tkinter import messagebox

def calculate():
    ip_cidr = entry.get()
    try:
        network = ipaddress.ip_network(ip_cidr, strict=False)
        hosts = list(network.hosts())
        result = f"Network Address: {network.network_address}\n"
        result += f"Broadcast Address: {network.broadcast_address}\n"
        result += f"Subnet Mask: {network.netmask}\n"
        result += f"CIDR Notation: /{network.prefixlen}\n"
        result += f"Number of Usable Hosts: {len(hosts)}\n"
        if hosts:
            result += f"First Usable IP: {hosts[0]}\n"
            result += f"Last Usable IP: {hosts[-1]}\n"
        output.config(state='normal')
        output.delete(1.0, tk.END)
        output.insert(tk.END, result)
        output.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Invalid IP/CIDR. Use format like 192.168.1.10/24")

root = tk.Tk()
root.title("Subnet Calculator")

tk.Label(root, text="Enter IP/CIDR (e.g., 192.168.1.10/24):").pack(pady=5)
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

output = tk.Text(root, width=50, height=10, state='disabled')
output.pack(pady=5)

root.mainloop()
