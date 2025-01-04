import psutil
import socket
import tkinter as tk
from tkinter import ttk

def get_system_status():
    """Collects and returns basic system status information."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    system_status = {
        "CPU Usage (%)": cpu_usage,
        "Memory Usage (%)": memory_info.percent,
        "Disk Usage (%)": disk_usage.percent
    }
    return system_status

def get_network_interfaces():
    """Returns a list of available network interfaces and their details."""
    interfaces = psutil.net_if_addrs()
    interface_details = {}
    for interface, addresses in interfaces.items():
        details = []
        for addr in addresses:
            if addr.family == socket.AF_LINK:  # MAC address
                details.append(f"MAC Address: {addr.address}")
            elif addr.family == socket.AF_INET:  # IPv4 address
                details.append(f"IPv4 Address: {addr.address}")
            elif addr.family == socket.AF_INET6:  # IPv6 address
                details.append(f"IPv6 Address: {addr.address}")
        interface_details[interface] = details
    return interface_details

def get_network_traffic():
    """Returns the total bytes sent and received by all network interfaces."""
    net_io = psutil.net_io_counters()
    traffic_data = {
        "Bytes Sent (MB)": round(net_io.bytes_sent / (1024 ** 2), 2),
        "Bytes Received (MB)": round(net_io.bytes_recv / (1024 ** 2), 2)
    }
    return traffic_data

def refresh_data():
    """Fetches and displays data on the GUI."""
    # Clear existing data in the text widgets
    system_status_text.delete(1.0, tk.END)
    network_interfaces_text.delete(1.0, tk.END)
    network_traffic_text.delete(1.0, tk.END)

    # Get data
    system_status = get_system_status()
    interfaces = get_network_interfaces()
    traffic = get_network_traffic()

    # Display system status
    system_status_text.insert(tk.END, "System Status:\n")
    for key, value in system_status.items():
        system_status_text.insert(tk.END, f"{key}: {value}\n")

    # Display network interfaces
    network_interfaces_text.insert(tk.END, "Network Interfaces:\n")
    for interface, details in interfaces.items():
        network_interfaces_text.insert(tk.END, f"{interface}:\n")
        for detail in details:
            network_interfaces_text.insert(tk.END, f"  {detail}\n")

    # Display network traffic
    network_traffic_text.insert(tk.END, "Network Traffic:\n")
    for key, value in traffic.items():
        network_traffic_text.insert(tk.END, f"{key}: {value} MB\n")

# Create the main Tkinter window
root = tk.Tk()
root.title("Network Monitoring Tool")
root.geometry("800x600")

# Create tabs using a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Create frames for each tab
system_status_frame = ttk.Frame(notebook)
network_interfaces_frame = ttk.Frame(notebook)
network_traffic_frame = ttk.Frame(notebook)

# Add frames as tabs
notebook.add(system_status_frame, text="System Status")
notebook.add(network_interfaces_frame, text="Network Interfaces")
notebook.add(network_traffic_frame, text="Network Traffic")

# Create text widgets for each tab to display data
system_status_text = tk.Text(system_status_frame, wrap=tk.WORD, height=25, width=80)
network_interfaces_text = tk.Text(network_interfaces_frame, wrap=tk.WORD, height=25, width=80)
network_traffic_text = tk.Text(network_traffic_frame, wrap=tk.WORD, height=25, width=80)

# Place text widgets in the frames
system_status_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
network_interfaces_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
network_traffic_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add a refresh button at the bottom
refresh_button = tk.Button(root, text="Refresh Data", command=refresh_data)
refresh_button.pack(pady=10)

# Populate data on startup
refresh_data()

# Run the Tkinter main loop
root.mainloop()