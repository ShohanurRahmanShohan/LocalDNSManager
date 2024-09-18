import os
import tkinter as tk
from tkinter import messagebox

def add_host_entry(domain, ip_address):
    hosts_path = "/etc/hosts" if os.name == "posix" else r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write(f"\n{ip_address} {domain}\n")
    messagebox.showinfo("Success", f"Added: {domain} -> {ip_address}")
    refresh_entries()

def remove_host_entry(domain):
    hosts_path = "/etc/hosts" if os.name == "posix" else r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()
    with open(hosts_path, 'w') as hosts_file:
        for line in lines:
            if not line.strip().endswith(domain):
                hosts_file.write(line)
    messagebox.showinfo("Success", f"Removed: {domain}")
    refresh_entries()

def list_host_entries():
    hosts_path = "/etc/hosts" if os.name == "posix" else r"C:\Windows\System32\drivers\etc\hosts"
    entries = []
    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()
        for line in lines:
            if not line.startswith('#') and line.strip():
                entries.append(line.strip())
    return entries

def add_entry():
    domain = domain_entry.get()
    ip_address = ip_entry.get()
    if domain and ip_address:
        add_host_entry(domain, ip_address)
    else:
        messagebox.showerror("Error", "Please enter both domain and IP address")

def remove_entry():
    domain = domain_entry.get()
    if domain:
        remove_host_entry(domain)
    else:
        messagebox.showerror("Error", "Please enter a domain")

def refresh_entries():
    entries = list_host_entries()
    text_widget.delete('1.0', tk.END)  
    for entry in entries:
        text_widget.insert(tk.END, entry + '\n')

root = tk.Tk()
root.title("Host File Manager")

tk.Label(root, text="Domain:").grid(row=0, column=0, padx=10, pady=10)
domain_entry = tk.Entry(root)
domain_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="IP Address:").grid(row=1, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root)
ip_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=2, column=0, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Entry", command=remove_entry)
remove_button.grid(row=2, column=1, padx=10, pady=10)

refresh_button = tk.Button(root, text="Refresh Entries", command=refresh_entries)
refresh_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

text_widget = tk.Text(root, height=10, width=50)
text_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

refresh_entries()  
root.mainloop()
